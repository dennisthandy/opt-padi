from django.conf import settings
import os
import numpy as np
import tensorflow as tf
# from tensorflow.keras.models import model_from_json
from helper.model import load_cnn_model, load_lvq_model
from helper.lvq import predict

labels = ['Brown Spot', 'Healthy', 'Hispa', 'Leaf Blast']

def cnn_predict(data):
    model = load_cnn_model()
    result = np.argmax(model.predict(data))

    return labels[result]


def lvq_predict(data):
    model = load_lvq_model()
    result = predict(data, model)

    return labels[result[0]]


'''model = tf.keras.models.load_model(os.path.join(settings.BASE_DIR, ('static/model.h5')))
model.load_weights(os.path.join(settings.BASE_DIR, ('static/weight.h5')))

model_json = open(os.path.join(settings.BASE_DIR, ('static/model.json')))
model = model_json.read()
model_json.close()

model = model_from_json(model)
model.load_weights(os.path.join(settings.BASE_DIR, ('static/weight.h5')))

model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=1e-3), loss='categorical_crossentropy', metrics='accuracy')

loaded_model = tf.keras.models.load_model(os.path.join(settings.BASE_DIR, ('static/model_128_100_cross_validation_fold_1.h5')))
loaded_model.load_weights(os.path.join(settings.BASE_DIR, ('static/weight_128_100_cross_validation_fold_1.h5')))'''
