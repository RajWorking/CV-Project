import io
import cv2 as cv
import keras.backend as K
import numpy as np
import PIL.Image as Image
from model import build_model_deconv, build_model, build_model_imagenette

from config import IMG_ROWS, IMG_COLS, EPSILON


def encode_image(image):
    is_success, im_buf_arr = cv.imencode(".jpg", image)
    print(is_success)
    byte_im = im_buf_arr.tobytes()
    return (byte_im)


def colorize(image, model_type=None, temp=None):


    gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    if model_type == 'deconv':
        model = build_model_deconv()
        model_weights_path = './models/'
    elif model_type == 'imagenette':
        model = build_model_imagenette()
        model_weights_path = './models/'
            
    elif model_type == 'landscape':
        model = build_model()
        model_weights_path = './models/'
    else:
        model_weights_path = './models/'
        model = build_model()
        print('Using default model')

    try:
        temp = float(temp)
    except:
        temp = 0.38
        print('Using temp as 0.38')


    model.load_weights(model_weights_path)

    h, w = IMG_ROWS // 4, IMG_COLS // 4

    # Load the array of quantized ab value
    q_ab = np.load("data/pts_in_lab_space.npy")
    nb_q = q_ab.shape[0]

    image = cv.resize(image, (IMG_ROWS, IMG_COLS), cv.INTER_CUBIC)
    gray_image = cv.resize(gray_image, (IMG_ROWS, IMG_COLS), cv.INTER_CUBIC)

    # L: 0 <=L<= 255, a: 42 <=a<= 226, b: 20 <=b<= 223.
    lab = cv.cvtColor(image, cv.COLOR_BGR2LAB)

    x_test = np.empty((1, IMG_ROWS, IMG_COLS, 1), dtype=np.float32)
    x_test[0, :, :, 0] = gray_image / 255.

    # L: 0 <=L<= 255, a: 42 <=a<= 226, b: 20 <=b<= 223.
    X_colorized = model.predict(x_test)
    X_colorized = X_colorized.reshape((h * w, nb_q))

    # Reweight probas
    X_colorized = np.exp(np.log(X_colorized + EPSILON) / temp)
    X_colorized = X_colorized / np.sum(X_colorized, 1)[:, np.newaxis]

    # Reweighted
    q_a = q_ab[:, 0].reshape((1, 313))
    q_b = q_ab[:, 1].reshape((1, 313))

    X_a = np.sum(X_colorized * q_a, 1).reshape((h, w))
    X_b = np.sum(X_colorized * q_b, 1).reshape((h, w))

    X_a = cv.resize(X_a, (IMG_ROWS, IMG_COLS), cv.INTER_CUBIC)
    X_b = cv.resize(X_b, (IMG_ROWS, IMG_COLS), cv.INTER_CUBIC)

    # Before: -90 <=a<= 100, -110 <=b<= 110
    # After: 38 <=a<= 228, 18 <=b<= 238
    X_a = X_a + 128
    X_b = X_b + 128

    out_lab = np.zeros((IMG_ROWS, IMG_COLS, 3), dtype=np.int32)
    out_lab[:, :, 0] = lab[:, :, 0]
    out_lab[:, :, 1] = X_a
    out_lab[:, :, 2] = X_b


    out_lab = out_lab.astype(np.uint8)
    out_bgr = cv.cvtColor(out_lab, cv.COLOR_LAB2BGR)
    out_bgr = out_bgr.astype(np.uint8)

    K.clear_session()

    cv.imwrite('./img.jpeg', image)
    cv.imwrite('./img_out.jpeg', image)

    return image, out_bgr
