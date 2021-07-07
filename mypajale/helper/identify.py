from django.conf import settings
import os
import numpy as np
import tensorflow as tf
# from tensorflow.keras.models import model_from_json
from helper.model import load_cnn_model, load_lvq_model
from helper.lvq import predict

labels = ['Brown Spot', 'Healthy', 'Hispa', 'Leaf Blast']
detail_labels = {
    0: 'Penyakit bercak daun coklat (brown leaf spot) pada tanaman padi (oryza sativa l) ini disebabkan oleh cendawan Helminthosporium oryzae atau Drechslera oryzae (Cochliobolus miyabeanus).',
    1: 'Kondisi daun berwarna hijau terang tanpa ada bercak.',
    2: 'Kerusakan disebabkan oleh serangga dewasa dan larva hispa padi, Dicladispa armigera. Serangga dewasa mengikis permukaan atas helai daun dan hanya menyisakan epidermis bawah.',
    3: 'Penyakit blas yang disebabkan oleh jamur Pyricularia oryzae Cav. [sinonim Magnaportheoryzae (Hebert) Barr] merupakan salah satu penyakit penting pada tanaman padi di seluruh dunia'
}

def cnn_predict(data):
    model = load_cnn_model()
    result = np.argmax(model.predict(data))

    return { 'name': labels[result], 'desc': detail_labels[result] }


def lvq_predict(data):
    model = load_lvq_model()
    result = predict(data, model)

    return { 'name': labels[result[0]], 'desc': detail_labels[result[0]] }


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
