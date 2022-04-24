import keras.backend as K
import numpy as np
import tensorflow as tf
prior_factor = np.load('data/prior_factor_60000.npy').astype(np.float32)

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

# getting the number of GPUs
def get_available_gpus():
    devices = tf.config.experimental.list_physical_devices('GPU')
    devices_names = [d.name.split('e:')[1] for d in devices]
    return devices_names
    # local_device_protos = device_lib.list_local_devices()
    # return [x.name for x in local_device_protos if x.device_type == 'GPU']

