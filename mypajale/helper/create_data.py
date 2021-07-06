import cv2, numpy as np
from helper.model import get_feature_model

def do_feature_learning(image):
    model = get_feature_model();

    data = model.predict(image);
    data = data.reshape(data.shape[0], data.shape[1] * data.shape[2] * data.shape[3])
    
    return data

def create_data(image):
    size = 64
    
    img_array = cv2.imread(image, cv2.IMREAD_COLOR) #convert image to array using cv2
    img_rgb = cv2.cvtColor(img_array, cv2.COLOR_BGR2RGB)  #convert to RGB channel
    img_resize = cv2.resize(img_rgb, (size, size), interpolation = cv2.INTER_AREA) #resize img array

    data = np.array(img_resize).reshape(-1, size, size, 3) #convert data to numpy array
    data = data / 255.0  # normalize 
    
    flatten_data = do_feature_learning(np.array(data))

    return {'cnn': data, 'lvq' : flatten_data}