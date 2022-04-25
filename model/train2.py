import argparse

import tensorflow as tf
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping, ReduceLROnPlateau

from config import BATCH_SIZE, PATIENCE, EPOCHS, TRAINING_SAMPLES, VALIDATION_SAMPLES
from data_generator import train_generator, valid_generator
from model import build_model
from utils import * 



if __name__ == '__main__':
    # Parse arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-p", "--pretrained", help="path to save pretrained model files")
    args = vars(ap.parse_args())
    pretrained_path = args["pretrained"]
    checkpoint_models_path = './models/'


    # Callbacks
    # tensor_board = keras.callbacks.TensorBoard(log_dir='./logs', histogram_freq=0, write_graph=True, write_images=True)
    model_names = checkpoint_models_path + 'model.{epoch:02d}-{val_loss:.4f}.hdf5'
    model_checkpoint = ModelCheckpoint(model_names, monitor='val_loss', verbose=1, save_best_only=True, save_weights_only=True, period=15)
    early_stop = EarlyStopping('val_loss', patience=PATIENCE)
    reduce_lr = ReduceLROnPlateau('val_loss', factor=0.1, patience=PATIENCE // 4, verbose=1)


#     class MyCbk(tf.keras.callbacks.Callback):
#         def __init__(self, model):
#             tf.keras.callbacks.Callback.__init__(self)
#             self.model_to_save = model

#             def on_epoch_end(self, epoch, logs=None):
# #                if (epoch + 1) % 15 == 0:
#                 fmt = checkpoint_models_path + 'model.%02d-%.4f.hdf5'
#                 self.model_to_save.save(fmt % (epoch, logs['val_loss']))
#                 print('Model saved')


    # Load our model, added support for Multi-GPUs
    devices = get_available_gpus()

    num_gpu = len(devices)
    mirrored_strategy = tf.distribute.MirroredStrategy(devices=devices)

    print(num_gpu)
    print(mirrored_strategy.num_replicas_in_sync)

    
    loss_controller = LossController()


    with mirrored_strategy.scope():
        model = build_model()
        # model_checkpoint = MyCbk(model)
        if pretrained_path is not None:
            model.load_weights(pretrained_path)
        sgd = tf.keras.optimizers.SGD(lr=0.0005, momentum=0.9, nesterov=True)
        model.compile(optimizer=sgd, loss=loss_controller.compute_loss) 
    

    print(model.summary())

    # Final callbacks
    callbacks = [model_checkpoint, early_stop, reduce_lr]

    # batch_size = BATCH_SIZE * num_gpu

    # Start Fine-tuning
    model.fit(train_generator(),
                            batch_size= BATCH_SIZE,    
                            validation_data=valid_generator(),
                            epochs=EPOCHS,
                            verbose=1,
                            callbacks=callbacks,
                            # use_multiprocessing=True,
                            #  workers=8
                            )

