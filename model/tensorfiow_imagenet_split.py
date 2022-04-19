import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf

import tensorflow_datasets as tfds

ds = tfds.load('imagenet2012_subset', split=['train', 'valid'], data_dir='./images', shuffle_files=True, download=True)
assert isinstance(ds, tf.data.Dataset)
print(ds)