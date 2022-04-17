import os
from turtle import color

import numpy as np
import random
import cv2
import sklearn.neighbors as nn
from scipy.interpolate import interp1d
from scipy.signal import gaussian, convolve

from config import IMAGENET_IMAGES_PATH, IMAGE_DIMENSIONS, INTERPOLATION_METHOD, NUM_OF_NEIGHBOURS, SMOOTHING_SIGMA, REBALANCING_GAMMA

def load_data(sample_size=10000, image_dimension=IMAGE_DIMENSIONS):
    images_path = IMAGENET_IMAGES_PATH
    names = [name for name in os.listdir(images_path) if name.contains('.jpg')]
    subsampled_names = random.sample(names, sample_size)
    color_channels = np.empty((sample_size, image_dimension, image_dimension, 2))
    for i, name in enumerate(subsampled_names):
        bgr = cv2.imread(f'{images_path}/{name}')
        ## If image is being downsampled
        if INTERPOLATION_METHOD == 'INTER_AREA':
            bgr = cv2.resize(bgr, (image_dimension, image_dimension), interpolation = cv2.INTER_AREA)
        else:
            bgr = cv2.resize(bgr, (image_dimension, image_dimension), interpolation = cv2.INTER_CUBIC)
        lab = cv2.cvtColor(bgr, cv2.COLOR_BGR2LAB)
        lab = lab.astype(np.int32) ## Do we need this
        color_channels[i] = lab[:, :, 1:] - 128
    return color_channels

def compute_color_prior_factor(color_channels, sigma=SMOOTHING_SIGMA, gamma=REBALANCING_GAMMA):
    ab_bins = np.load('data/pts_in_lab_space.npy')
    color_channels = color_channels.reshape(-1, 2)
    ## Find bins for each color pixels
    nearest = nn.NearestNeighbors(n_neighbors=NUM_OF_NEIGHBOURS, algorithm='ball_tree').fit(ab_bins) # Can use algorithm='auto'
    _, indexs = nearest.kneighbours(color_channels)
    pos_prob = np.bincount(indexs.flatten())
    pos_indxes = np.unique(indexs)

    prior_prob = np.zeros((313))
    prior_prob[pos_indxes] = pos_prob[pos_indxes]

    # np.save('data/prior_prob.npy', prior_prob)

    prior_prob += 1e-3 * np.min(prior_prob)
    # We turn this into a color probability
    prior_prob = prior_prob / (1.0 * np.sum(prior_prob))

    f = interp1d(np.arange(prior_prob.shape[0]), prior_prob)
    xx = np.linspace(0, prior_prob.shape[0] - 1, 1000)
    yy = f(xx)
    window = gaussian(2000, sigma)  # 2000 pts in the window, sigma=5
    smoothed = convolve(yy, window / window.sum(), mode='same')
    fout = interp1d(xx, smoothed)
    prior_prob_smoothed = np.array([fout(i) for i in range(prior_prob.shape[0])])
    prior_prob_smoothed = prior_prob_smoothed / np.sum(prior_prob_smoothed)

    prior_factor = 1/((1-gamma) * prior_prob_smoothed + gamma / 313)
    prior_factor = prior_factor / (np.sum(prior_factor * prior_prob_smoothed))

    np.save('data/prior_factor.npy', prior_factor)

    if __name__ == '__main__':
        color_channels = load_data()
        compute_color_prior_factor(color_channels=color_channels)

