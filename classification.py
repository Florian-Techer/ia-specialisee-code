import numpy as np
from PIL import Image
import cv2
# TensorFlow and tf.keras
from tensorflow.keras.applications.imagenet_utils import
preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import
MobileNetV2