import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf

import tensorflow_datasets as tfds

ds, ds_info = tfds.load('imagenet2012_subset/10pct', split=['train', 'validation'], data_dir='./images', shuffle_files=True, download=True, with_info=True)
# assert isinstance(ds, tf.data.Dataset)
# fig = tfds.show_examples(ds, ds_info)
# print(ds)