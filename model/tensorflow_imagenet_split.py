import tensorflow_datasets as tfds

ds, ds_info = tfds.load('imagenette', split='all', data_dir='./images', download=True, with_info=True)
