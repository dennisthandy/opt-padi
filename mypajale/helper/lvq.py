import numpy as np

#euclideian distance function
def euclideanDistance(data, weights):
	result = [np.sqrt(np.sum(np.square(data - weight))) for weight in weights ]
	return result

#function test our trained lvq model
def predict(test, model):
	predictions = []
	for data in test:
		distance = euclideanDistance(data, model) #get all distance
		output = np.argmin(distance) #choose minimum distance
		predictions.append(output) #save to array
	
	return np.array(predictions) #return array predictions