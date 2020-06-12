# -*- coding: utf-8 *-*

import numpy as np
import time


class Perceptron():
	def __init__(self, inputs=1):
		""" Инициализация весов """
		self.weights = 2 * np.random.rand(inputs).T - 1 # Веса, -1 > w < 1

	def predict(self, x):
		""" Предсказание сети """
		y = self.activation(np.dot(x, self.weights))
		return y

	def train(self, X, Y, epochs=1, lr=1):
		""" Обучаем наш перцептрон """
		T0 = time.time()
		for i in range(epochs):
			t0 = time.time()
			for j in range(len(X)):
				x = X[j]
				y = Y[j]

				y_predict = self.predict(x)

				err = (y - y_predict)
				delta_weight = err * self.activation(y_predict, True)

				self.weights += x * (delta_weight * lr)

				print("\rEpoch #{} - error: {} - time {}sec.".format(i + 1, err, round(t0 - time.time(), 3)))
		print("Total - error: {} - time {}sec.".format(err, round(T0 - time.time(), 3)))


	def activation(self, x, deriv=False):
		""" Функция активации (сигмоида) """
		if deriv:
			return self.activation(x) * (1 - self.activation(x))
		return  1 / (1 + np.exp(-x)) 


if __name__ == '__main__':
	X = np.array([[0,0,1],
	            [0,1,0],
	            [1,1,0],
	            [1,1,1]])
	                
	Y = np.array([[1],
				[0],
				[1],
				[1]])

	perceptron = Perceptron(inputs=3)

	perceptron.train(X, Y, epochs=10000, lr=.01)

	[print(perceptron.predict(np.array(x))) for x in X]