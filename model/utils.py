import keras.backend as K
import numpy as np

prior_factor = np.load('data/prior_factor.npy').astype(np.float32)

def categorical_crossentropy_color(y_pred, y_true):
    bins = 313
    y_true = K.reshape(y_true, (-1, bins))
    y_pred = K.reshape(y_pred, (-1, bins))

    max_idx = K.argmax(y_true, axis=1)
    weights = K.gather(prior_factor, max_idx)
    weights = K.reshape(weights, (-1, 1))

    y_true = y_true * weights

    cross_entropy = K.categorical_crossentropy(y_pred, y_true)
    cross_entropy = K.mean(cross_entropy, axis=-1)

    return cross_entropy