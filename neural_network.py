# -*- coding: utf-8 *-*
import numpy as np
import time


def sigmoid(x, deriv=False):
	if deriv:
		return sigmoid(x) * (1 - sigmoid(x))
	return 1 / (1 + np.exp(-x))


class NeuralNetwork():
	def __init__(self, inputs=1, layers=[]):
		self.layers = [inputs] + layers
		self.weights = [2 * np.random.random([inputs, layers[0]]) - 1]

		for layer in range(1, len(layers)):
			self.weights.append(2 * np.random.random([layers[layer - 1], layers[layer]]) - 1)


	def predict(self, x):
		y = x
		for layer in self.weights:
			y = sigmoid(np.dot(y, layer))
		return y

	def train(self, X, Y, epochs=1, batch_size=1, lr=1):
		T0 = time.time()
		for epoch in range(epochs):
			t0 = time.time()
			print("Epoch #{}".format(epoch), end="\r")

			for i in range(len(X) // batch_size):
				x = X[batch_size * i: batch_size * (i + 1)]
				y = Y[batch_size * i: batch_size * (i + 1)]

				layers_outputs = [x]
				for layer in self.weights:
					layers_outputs.append(sigmoid(np.dot(layers_outputs[-1], layer)))

				y_predict = layers_outputs[-1]
				err = y - y_predict
				ERROR = err.sum()

				for l in range(len(self.weights) - 1, -1, -1):
					delta = err * sigmoid(layers_outputs[l + 1])
					err = delta.dot(self.weights[l].T)
					self.weights[l] += layers_outputs[l].T.dot(delta) * lr

				dtime = time.time() - t0
				print("Epoch #{} - {}/{}  Error: {}  time: {}s({}m) time left: ~{}s({}m)   ".format(epoch + 1, 
															batch_size * i,
															len(X), 
															round(ERROR, 2), 
															round(dtime, 2), 
																round(dtime / 60, 1),
															round(dtime / (i + 1) * (len(X) // batch_size) - dtime, 2), 
																round((dtime / (i + 1) * (len(X) // batch_size) - dtime) / 60, 1)),
														end="\r")

			print("\rEpoch #{} - Error: {}  time: {}s.".format(epoch + 1, round(ERROR, 2), round(time.time() - t0), 2))
		Time = time.time() - T0
		print("Total - Error: {} - Time spend: {}s({}m)".format(round(ERROR, 2), round(Time, 2), round(Time / 60, 1)))

	def info(self):
		info = "-"*16 + "\nInputs: {}\n".format(self.layers[0])

		for i in self.layers[1:]:
			info = info + "Layer: {} neurons\n".format(i)
		info = info + "-" * 16
		return info



if __name__ == '__main__':
	import mnist
	m = mnist.MNIST("samples")
	X, Y = m.load_training()

	trainX = np.array(X) / 256
	trainY = np.array([[0] * y + [1] + [0] * (9-y) for y in Y])
	print("READY!")


	np.random.seed(1)

	mnist_model = NeuralNetwork(inputs=784, layers=[800, 10])
	print(mnist_model.info())
	mnist_model.train(trainX, trainY, epochs=20, batch_size=250, lr=.01)


	test = m.load_testing()
	x, y = np.array(test[0]) / 256, test[1]

	right, lose = 0, 0
	for i in range(len(x)):
	    predict = mnist_model.predict(x[i])
	    ans = predict.tolist().index(max(predict))
	    
	    if ans == y[i]:
	        right += 1
	    else:
	        lose += 1
	    print("#" + str(i) + " - Right - {} ({}%);  Lose - {} ({}%);".format(
	        right, right / (i + 1) * 100 ,
	        lose, lose / (i + 1) * 100 ), end="\r")