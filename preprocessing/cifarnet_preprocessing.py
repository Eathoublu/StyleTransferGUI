

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf

_PADDING = 4

slim = tf.contrib.slim


def preprocess_for_train(image,
                         output_height,
                         output_width,
                         padding=_PADDING):

  tf.image_summary('image', tf.expand_dims(image, 0))

  # Transform the image to floats.
  image = tf.to_float(image)
  if padding > 0:
    image = tf.pad(image, [[padding, padding], [padding, padding], [0, 0]])
  # Randomly crop a [height, width] section of the image.
  distorted_image = tf.random_crop(image,
                                   [output_height, output_width, 3])

  # Randomly flip the image horizontally.
  distorted_image = tf.image.random_flip_left_right(distorted_image)

  tf.image_summary('distorted_image', tf.expand_dims(distorted_image, 0))

  # Because these operations are not commutative, consider randomizing
  # the order their operation.
  distorted_image = tf.image.random_brightness(distorted_image,
                                               max_delta=63)
  distorted_image = tf.image.random_contrast(distorted_image,
                                             lower=0.2, upper=1.8)
  # Subtract off the mean and divide by the variance of the pixels.
  return tf.image.per_image_whitening(distorted_image)


def preprocess_for_eval(image, output_height, output_width):

  tf.image_summary('image', tf.expand_dims(image, 0))
  # Transform the image to floats.
  image = tf.to_float(image)

  # Resize and crop if needed.
  resized_image = tf.image.resize_image_with_crop_or_pad(image,
                                                         output_width,
                                                         output_height)
  tf.image_summary('resized_image', tf.expand_dims(resized_image, 0))

  # Subtract off the mean and divide by the variance of the pixels.
  return tf.image.per_image_whitening(resized_image)


def preprocess_image(image, output_height, output_width, is_training=False):

  if is_training:
    return preprocess_for_train(image, output_height, output_width)
  else:
    return preprocess_for_eval(image, output_height, output_width)
