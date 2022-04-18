import keras.backend as K
import tensorflow as tf
from tensorflow import keras
from keras.layers import Conv2D, BatchNormalization, UpSampling2D
# from keras.models import Model
# from keras.regularizers import l2
from keras.utils import multi_gpu_model
from keras.utils import plot_model

# from config import img_rows, img_cols, num_classes, kernel

# l2_reg = l2(1e-3)


###
# Doesn't use kernel initializer = 'he_normal'
# Doesn't use kernel initializer = l2(1e-3) from keras.regularizers 
###

def build_model(kernel=3):

    const_params = {
        'activation': 'relu',
        'use_bias': True,
        'padding': 'same'
    }

    model = keras.Sequential([

        Conv2D(64, kernel, strides=1, dilation_rate=1, name='conv1_1', **const_params),
        Conv2D(64, kernel, strides=2, dilation_rate=1, name='conv1_2', **const_params),
        BatchNormalization(),


        Conv2D(128, kernel, strides=1, dilation_rate=1, name='conv2_1', **const_params),
        Conv2D(128, kernel, strides=2, dilation_rate=1, name='conv2_2', **const_params),
        BatchNormalization(),


        Conv2D(256, kernel, strides=1, dilation_rate=1, name='conv3_1', **const_params),
        Conv2D(256, kernel, strides=1, dilation_rate=1, name='conv3_2', **const_params),
        Conv2D(256, kernel, strides=2, dilation_rate=1, name='conv3_3', **const_params),
        BatchNormalization(),


        Conv2D(512, kernel, strides=1, dilation_rate=1, name='conv4_1', **const_params),
        Conv2D(512, kernel, strides=1, dilation_rate=1, name='conv4_2', **const_params),
        Conv2D(512, kernel, strides=1, dilation_rate=1, name='conv4_3', **const_params),
        BatchNormalization(),


        Conv2D(512, kernel, strides=1, dilation_rate=2, name='conv5_1', **const_params),
        Conv2D(512, kernel, strides=1, dilation_rate=2, name='conv5_2', **const_params),
        Conv2D(512, kernel, strides=1, dilation_rate=2, name='conv5_3', **const_params),
        BatchNormalization(),

        
        Conv2D(512, kernel, strides=1, dilation_rate=2, name='conv6_1', **const_params),
        Conv2D(512, kernel, strides=1, dilation_rate=2, name='conv6_2', **const_params),
        Conv2D(512, kernel, strides=1, dilation_rate=2, name='conv6_3', **const_params),
        BatchNormalization(),

        Conv2D(256, kernel, strides=1, dilation_rate=1, name='conv7_1', **const_params),
        Conv2D(256, kernel, strides=1, dilation_rate=1, name='conv7_2', **const_params),
        Conv2D(256, kernel, strides=1, dilation_rate=1, name='conv7_3', **const_params),
        BatchNormalization(),


        UpSampling2D(size=2),
        Conv2D(128, kernel, strides=1, dilation_rate=1, name='conv8_1', **const_params),
        Conv2D(128, kernel, strides=1, dilation_rate=1, name='conv8_2', **const_params),
        Conv2D(128, kernel, strides=1, dilation_rate=1, name='conv8_3', **const_params),


        Conv2D(313, 1, activation='softmax', strides=1, padding=0, name='loss_layer')

    ])

    print(model.summary())

    return model


if __name__ == '__main__':
    with tf.device("/cpu:0"):
        encoder_decoder = build_model()
    print(encoder_decoder.summary())
    plot_model(encoder_decoder, to_file='encoder_decoder.svg', show_layer_names=True, show_shapes=True)

    parallel_model = multi_gpu_model(encoder_decoder, gpus=None)
    print(parallel_model.summary())
    plot_model(parallel_model, to_file='parallel_model.svg', show_layer_names=True, show_shapes=True)

    K.clear_session()