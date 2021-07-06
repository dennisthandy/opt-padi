from django.conf import settings
import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import model_from_json

def load_cnn_model():
    model = tf.keras.models.load_model(
        os.path.join(
            settings.BASE_DIR, ('static/cnn/model_64x64.h5')
    ))
    model.load_weights(
        os.path.join(
            settings.BASE_DIR, ('static/cnn/weight_64x64.h5')
    ))

    return model

def load_lvq_model():
    data = np.load(os.path.join(
        settings.BASE_DIR, ('static/lvq/model_64x64_data.npz')
    ))

    return data['arr_0']

def get_feature_model():
    model = load_cnn_model()

    input_layer = model.get_layer(name="input_layer").input
    feature_layer = model.get_layer(name='feature_layer').output
    feature_model = tf.keras.models.Model(input_layer, feature_layer)

    return feature_model