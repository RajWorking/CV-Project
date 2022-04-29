from tensorflow.keras import Sequential
from keras.layers import Conv2D, BatchNormalization, UpSampling2D, Input, Conv2DTranspose

from config import IMG_ROWS, IMG_COLS

const_params = {
    'activation': 'relu',
    'use_bias': True,
    'padding': 'same',
    'kernel_size': 3
}

def build_model():


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

        Conv2D(256, strides=1, dilation_rate=1, name='conv7_1', **const_params),
        Conv2D(256, strides=1, dilation_rate=1, name='conv7_2', **const_params),
        Conv2D(256, strides=1, dilation_rate=1, name='conv7_3', **const_params),

        BatchNormalization(),

        UpSampling2D(size=(2, 2)),
        Conv2D(128, strides=1, dilation_rate=1, name='conv8_1', **const_params),
        Conv2D(128, strides=1, dilation_rate=1, name='conv8_2', **const_params),
        Conv2D(128, strides=1, dilation_rate=1, name='conv8_3', **const_params),
        BatchNormalization(),

        Conv2D(313, kernel_size=1, activation='softmax', strides=1, padding='valid', name='loss_layer', use_bias=True),


    ])

    return model


def build_model_deconv():

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

        Conv2D(512, strides=1, dilation_rate=1, name='conv7_1', **const_params),
        Conv2D(512, strides=1, dilation_rate=1, name='conv7_2', **const_params),
        Conv2D(512, strides=1, dilation_rate=1, name='conv7_3', **const_params),
        BatchNormalization(),


        Conv2DTranspose(256, kernel_size=4, strides=2, padding='same', name='conv8_1', activation='relu', use_bias=True),
        Conv2D(256, strides=1, dilation_rate=1, name='conv8_2', **const_params),
        Conv2D(256, strides=1, dilation_rate=1, name='conv8_3', **const_params),
        BatchNormalization(),


        Conv2DTranspose(128, kernel_size=4, strides=2, padding='same', name='conv9_1', activation='relu', use_bias=True),
        Conv2D(128, strides=1, dilation_rate=1, name='conv9_2', **const_params),
        Conv2D(128, strides=1, dilation_rate=1, name='conv9_3', **const_params),

        Conv2D(313, kernel_size=1, activation='softmax', strides=1, padding='valid', name='loss_layer', use_bias=True),

    ])

    return model
