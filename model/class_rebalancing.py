import os

import numpy as np
import random
import cv2

from config import IMAGENET_IMAGES_PATH, IMAGE_DIMENSIONS, INTERPOLATION_METHOD

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