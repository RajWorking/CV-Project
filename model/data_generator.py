
import os
from random import shuffle, sample

import numpy as np
import cv2
import sklearn.neighbors as nn
from tensorflow.keras.utils import Sequence

from config import IMAGENET_IMAGES_PATH, NUM_OF_NEIGHBOURS, IMG_ROWS, IMG_COLS, BATCH_SIZE, IMAGE_TRAIN_PATH, IMAGE_VALID_PATH

def get_soft_encoding(image_ab, nn_finder, bin_size):
    h, w = image_ab.shape[:2]
    ab = image_ab.reshape(-1, 2)
    dist, idx = nn_finder.kneighbors(ab)
    sigma = 5
    wts = np.exp(-dist ** 2 / (2 * sigma ** 2))
    wts = wts / np.sum(wts, axis=1)[:, np.newaxis]
    y = np.zeros((ab.shape[0], bin_size))
    idx_pts = np.arange(ab.shape[0])[:, np.newaxis]
    y[idx_pts, idx] = wts
    y = y.reshape(h, w, bin_size)
    return y


class DataSequenceGenerator(Sequence):
    def __init__(self, type) -> None:
        self.type = type
        if type == 'train':
            file_name = IMAGE_TRAIN_PATH
        else:
            file_name = IMAGE_VALID_PATH
        
        with open(file_name, 'r') as f:
            self.names = f.read().splitlines()
        
        self.num_samples = len(self.names)
        shuffle(self.names)

        ab_bins = np.load('data/pts_in_hull.npy')
        self.bin_size = ab_bins.shape[0]
        self.nn_finder = nn.NearestNeighbors(n_neighbors=NUM_OF_NEIGHBOURS, algorithm='ball_tree').fit(ab_bins)

    def __len__(self) -> int:
        return int(np.ceil(len(self.names) / BATCH_SIZE))

    def __getitem__(self, idx):
        done = idx * BATCH_SIZE
        out_img_rows, out_img_cols = IMG_ROWS // 4, IMG_COLS // 4
        data_sample_len = min(BATCH_SIZE, (self.num_samples - done))
        batch_x = np.empty((data_sample_len, IMG_ROWS, IMG_COLS, 1), dtype=np.float32)
        # batch_y = np.empty((data_sample_len, out_img_rows, out_img_cols, 2), dtype=np.float32)
        batch_encoding = np.empty((data_sample_len, out_img_rows, out_img_cols, self.bin_size), dtype=np.float32)

        # for i_batch in range(data_sample_len):
        #     image_name = self.names[done+i_batch]
        #     image_path = f'{IMAGENET_IMAGES_PATH}/{image_name}'
        #     bgr = cv2.imread(image_path)
        #     gray = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        #     gray = cv2.resize(gray, (IMG_ROWS, IMG_COLS), cv2.INTER_AREA)
        #     lab = cv2.cvtColor(bgr, cv2.COLOR_BGR2LAB)
        #     out_lab = cv2.resize(lab, (out_img_rows, out_img_cols), interpolation = cv2.INTER_AREA)
        #     out_ab = out_lab[:, :, 1:].astype(np.int32) - 128
        #     x = gray / 255.
        #     y = get_soft_encoding(out_ab, self.nn_finder, self.bin_size)

        #     if np.random.random() > 0.5:
        #         x = np.fliplr(x)
        #         y = np.fliplr(y)

        #     batch_x[i_batch, :, :, 0] = x
        #     batch_y[i_batch] = y
        

        for i_batch in range(data_sample_len):
            image_name = self.names[done+i_batch]
            image_path = f'{IMAGENET_IMAGES_PATH}/{image_name}'
            bgr = cv2.imread(image_path)
            bgr_resized = cv2.resize(bgr, (IMG_ROWS, IMG_COLS), interpolation = cv2.INTER_AREA)

            # if np.random.random() > 0.5:
            #     x = np.fliplr(x)
            #     y = np.fliplr(y)

            lab = cv2.cvtColor(bgr_resized, cv2.COLOR_BGR2LAB)
            lab_resized = cv2.resize(lab, (out_img_rows, out_img_cols), interpolation = cv2.INTER_AREA)
            lab_resized_ab = lab_resized[:,:,1:].astype('int32') - 128
            in_l = ((lab[:, :, 0].astype(np.float32) * 100 / 255) - 50).astype('int32')

            # print(in_l.shape)
            encoding = get_soft_encoding(lab_resized_ab, self.nn_finder, self.bin_size)

            batch_x[i_batch, :, :, 0] = in_l
            # batch_y[i_batch] = lab_resized_ab
            batch_encoding[i_batch] = encoding

        
        return batch_x, batch_encoding

    def on_epoch_end(self):
        np.random.shuffle(self.names)


        

def train_generator():
    return DataSequenceGenerator(type='train')

def valid_generator():
    return DataSequenceGenerator(type='valid')




def split_data():
    images_path = IMAGENET_IMAGES_PATH
    names = [name for name in os.listdir(images_path) if name.endswith('.JPEG')]

    num_samples = len(names)
    print(f'Total number of images: {num_samples}')
    print('Splitting images in 99.2% train and 0.8% validation dataset...')
    num_train_samples = int(num_samples * 0.992)
    print('num_train_samples: ' + str(num_train_samples))
    num_valid_samples = num_samples - num_train_samples
    print('num_valid_samples: ' + str(num_valid_samples))
    valid_names = sample(names, num_valid_samples)
    train_names = [n for n in names if n not in valid_names]
    shuffle(valid_names)
    shuffle(train_names)

    with open('valid_names.txt', 'w') as file:
        file.write('\n'.join(valid_names))

    with open('train_names.txt', 'w') as file:
        file.write('\n'.join(train_names))

if __name__ == '__main__':
    split_data()
