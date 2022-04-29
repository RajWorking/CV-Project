import keras.backend as K
import tensorflow as tf
from keras.layers import Conv2D, BatchNormalization, UpSampling2D, Input, Conv2DTranspose
from tensorflow.keras.regularizers import l2
from tensorflow.keras import Sequential

from config import IMG_ROWS, IMG_COLS

# l2_reg = l2(1e-3)


###
# Doesn't use kernel initializer = 'he_normal'
# Doesn't use kernel initializer = l2(1e-3) from keras.regularizers 
###

def build_model(kernel=3):

    const_params = {
        'activation': 'relu',
        'use_bias': True,
        'padding': 'same',
        'kernel_size': 3,
        'kernel_initializer': 'he_normal',
        'kernel_regularizer': l2(1e-3)
    }

    model = Sequential([
        Input(shape=(IMG_ROWS, IMG_COLS, 1)),

        Conv2D(64, strides=1, dilation_rate=1, name='conv1_1', **const_params),
        Conv2D(64, strides=2, dilation_rate=1, name='conv1_2', **const_params),
        BatchNormalization(),


        Conv2D(128, strides=1, dilation_rate=1, name='conv2_1', **const_params),
        Conv2D(128, strides=2, dilation_rate=1, name='conv2_2', **const_params),
        BatchNormalization(),


        Conv2D(256, strides=1, dilation_rate=1, name='conv3_1', **const_params),
        Conv2D(256, strides=1, dilation_rate=1, name='conv3_2', **const_params),
        Conv2D(256, strides=2, dilation_rate=1, name='conv3_3', **const_params),
        BatchNormalization(),


        Conv2D(512, strides=1, dilation_rate=1, name='conv4_1', **const_params),
        Conv2D(512, strides=1, dilation_rate=1, name='conv4_2', **const_params),
        Conv2D(512, strides=1, dilation_rate=1, name='conv4_3', **const_params),
        BatchNormalization(),


        Conv2D(512, strides=1, dilation_rate=2, name='conv5_1', **const_params),
        Conv2D(512, strides=1, dilation_rate=2, name='conv5_2', **const_params),
        Conv2D(512, strides=1, dilation_rate=2, name='conv5_3', **const_params),
        BatchNormalization(),

        
        Conv2D(512, strides=1, dilation_rate=2, name='conv6_1', **const_params),
        Conv2D(512, strides=1, dilation_rate=2, name='conv6_2', **const_params),
        Conv2D(512, strides=1, dilation_rate=2, name='conv6_3', **const_params),
        BatchNormalization(),

        # Conv2D(512, strides=1, dilation_rate=1, name='conv7_1', **const_params),
        # Conv2D(512, strides=1, dilation_rate=1, name='conv7_2', **const_params),
        # Conv2D(512, strides=1, dilation_rate=1, name='conv7_3', **const_params),
        Conv2D(256, strides=1, dilation_rate=1, name='conv7_1', **const_params),
        Conv2D(256, strides=1, dilation_rate=1, name='conv7_2', **const_params),
        Conv2D(256, strides=1, dilation_rate=1, name='conv7_3', **const_params),

        BatchNormalization(),

        
        # Conv2DTranspose(256, kernel_size=4, strides=2, padding='same', name='conv8_1', activation='relu', use_bias=True),
        # Conv2D(256, strides=1, dilation_rate=1, name='conv8_2', **const_params),
        # Conv2D(256, strides=1, dilation_rate=1, name='conv8_3', **const_params),

        UpSampling2D(size=(2, 2)),
        Conv2D(128, strides=1, dilation_rate=1, name='conv8_1', **const_params),
        Conv2D(128, strides=1, dilation_rate=1, name='conv8_2', **const_params),
        Conv2D(128, strides=1, dilation_rate=1, name='conv8_3', **const_params),
        BatchNormalization(),

        Conv2D(313, kernel_size=1, activation='softmax', strides=1, padding='valid', name='loss_layer', use_bias=True),

        # Conv2D(2, kernel_size=1, strides=1, dilation_rate=1, padding='valid', name='output', use_bias=False),
        

    ])

    return model


if __name__ == '__main__':
    with tf.device("/cpu:0"):
        encoder_decoder = build_model()
    print(encoder_decoder.summary())
    # plot_model(encoder_decoder, to_file='encoder_decoder.svg', show_layer_names=True, show_shapes=True)

    K.clear_session()