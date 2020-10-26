from django.conf import settings
import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import model_from_json

def predict(data):
    labels = ['Brown Spot', 'Healthy', 'Hispa', 'Leaf Blast']

    # model = tf.keras.models.load_model(os.path.join(settings.BASE_DIR, ('static/model.h5')))
    # model.load_weights(os.path.join(settings.BASE_DIR, ('static/weight.h5')))

    model_json = open(os.path.join(settings.BASE_DIR, ('static/model.json')))
    model = model_json.read()
    model_json.close()

    model = model_from_json(model)
    model.load_weights(os.path.join(settings.BASE_DIR, ('static/weight.h5')))

    model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=1e-3), loss='categorical_crossentropy', metrics='accuracy')

    result = np.argmax(model.predict(data))

    return labels[result]

