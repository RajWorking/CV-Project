import tensorflow_datasets as tfds

ds, ds_info = tfds.load('imagenet2012_subset/10pct', split='all', data_dir='./images', download=True, with_info=True)
