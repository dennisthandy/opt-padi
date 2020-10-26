import cv2, numpy as np

def create_data(image):
    imgArray = cv2.imread(image, cv2.IMREAD_COLOR) #convert image to array using cv2
    imgArray = cv2.cvtColor(imgArray, cv2.COLOR_BGR2RGB)  #convert to RGB channel
    sizedImgArray = cv2.resize(imgArray, (256, 256)) #resize img array

    data = np.array(sizedImgArray).reshape(-1, 256, 256, 3) #convert data to numpy array
    data = data / 255.0  # normalize data
    # data = np.expand_dims(data, 0)

    return data