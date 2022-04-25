import keras.backend as K
import numpy as np
import tensorflow as tf

import sklearn.neighbors as nn
from config import  NUM_OF_NEIGHBOURS


# prior_factor = np.load('data/prior_factor_60000.npy').astype(np.float32)

# def categorical_crossentropy_color(y_pred, y_true):
#     bins = 313
#     y_true = K.reshape(y_true, (-1, bins))
#     y_pred = K.reshape(y_pred, (-1, bins))

#     max_idx = K.argmax(y_true, axis=1)
#     weights = K.gather(prior_factor, max_idx)
#     weights = K.reshape(weights, (-1, 1))

#     y_true = y_true * weights

#     cross_entropy = K.categorical_crossentropy(y_pred, y_true)
#     cross_entropy = K.mean(cross_entropy, axis=-1)

#     return cross_entropy

# getting the number of GPUs
def get_available_gpus():
    devices = tf.config.experimental.list_physical_devices('GPU')
    devices_names = [d.name.split('e:')[1] for d in devices]
    return devices_names
    # local_device_protos = device_lib.list_local_devices()
    # return [x.name for x in local_device_protos if x.device_type == 'GPU']



class LossController():

    def __init__(self) -> None:
        self.thresh = 5
        self.setup_soft_encoding()
        self.setup_prior_factor()


    # def categorical_crossentropy_color(self, y_pred, y_true):
    #     bins = self.bin_size
    #     y_true = K.reshape(y_true, (-1, bins))
    #     y_pred = K.reshape(y_pred, (-1, bins))

    #     max_idx = K.argmax(y_true, axis=1)
    #     weights = K.gather(self.prior_factor, max_idx)
    #     weights = K.reshape(weights, (-1, 1))

    #     y_true = y_true * weights

    #     cross_entropy = K.categorical_crossentropy(y_pred, y_true)
    #     cross_entropy = K.mean(cross_entropy, axis=-1)

    #     return cross_entropy

    def compute_loss(self, y_true, y_pred):
        """
            y_true: B x H x W x 2
            y_pred: B x H x W x Q
        """

        gt_313_ab_quant = np.empty(y_pred.shape, dtype=np.float32)
        for i, data_ab in enumerate(y_true):
            gt_313_ab_quant[i] = self.get_soft_encoding(data_ab)

        gt_313_ab_quant = K.reshape(gt_313_ab_quant, (-1, self.bin_size))
        y_pred = K.reshape(y_pred, (-1, self.bin_size))

        max_idx = K.argmax(y_true, axis=1)
        weights = K.gather(self.prior_factor, max_idx)
        weights = K.reshape(weights, (-1, 1)) 

        y_true *= weights 

        cross_entropy = K.categorical_crossentropy(y_pred, y_true)
        cross_entropy = K.mean(cross_entropy, axis=-1)

        return cross_entropy
    
    # def get_non_gray_mask(self, data_ab):
    #     return (np.sum(np.sum(np.sum(np.abs(data_ab) > self.thresh,axis=1),axis=1),axis=1) > 0)[:,None,None,None]

    def setup_soft_encoding(self):
        ab_bins = np.load('data/pts_in_hull.npy')
        self.bin_size = ab_bins.shape[0]
        self.self.nn_finder = nn.NearestNeighbors(n_neighbors=NUM_OF_NEIGHBOURS, algorithm='ball_tree').fit(ab_bins)


    def get_soft_encoding(self, image_ab):
        h, w = image_ab.shape[:2]
        ab = image_ab.reshape(-1, 2)
        dist, idx = self.nn_finder.kneighbors(ab)
        sigma = 5
        wts = np.exp(-dist ** 2 / (2 * sigma ** 2))
        wts = wts / np.sum(wts, axis=1)[:, np.newaxis]
        y = np.zeros((ab.shape[0], self.bin_size))
        idx_pts = np.arange(ab.shape[0])[:, np.newaxis]
        y[idx_pts, idx] = wts
        y = y.reshape(h, w, self.bin_size)
        return y

    ''' Class handles prior factor '''
    def setup_prior_factor(self,alpha=1,gamma=0,verbose=True,priorFile='./data/prior_probs.npy'):
        # INPUTS
        #   alpha           integer     prior correction factor, 0 to ignore prior, 1 to divide by prior, alpha to divide by prior**alpha
        #   gamma           integer     percentage to mix in uniform prior with empirical prior
        #   priorFile       file        file which contains prior probabilities across classes

        # settings
        self.alpha = alpha
        self.gamma = gamma
        self.verbose = verbose

        # empirical prior probability
        self.prior_probs = np.load(priorFile)

        # define uniform probability
        self.uni_probs = np.zeros_like(self.prior_probs)
        self.uni_probs[self.prior_probs!=0] = 1.
        self.uni_probs = self.uni_probs/np.sum(self.uni_probs)

        # convex combination of empirical prior and uniform distribution       
        self.prior_mix = (1-self.gamma)*self.prior_probs + self.gamma*self.uni_probs

        # set prior factor
        self.prior_factor = self.prior_mix**-self.alpha
        self.prior_factor = self.prior_factor/np.sum(self.prior_probs*self.prior_factor) # re-normalize

        # implied empirical prior
        # self.implied_prior = self.prior_probs*self.prior_factor
        # self.implied_prior = self.implied_prior/np.sum(self.implied_prior)

    # def forward(self,data_ab_quant,axis=1):
    #     data_ab_maxind = np.argmax(data_ab_quant,axis=axis)
    #     corr_factor = self.prior_factor[data_ab_maxind]
    #     return corr_factor[:,None,:]
    #     # return K.reshape(corr_factor, (-1, 1))