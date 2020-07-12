# -*- coding: utf-8 -*-
# Всем привет! В этом видео мы будем рисовать папоротник Барнсли
# На python, используя библиотеку pygame
import pygame
pygame.init() # Импортируем и инициализируем pygame
import numpy as np
import random # Так же импортируем нужные нам библиотеки помимо pygame

# Создадим функцию, которая будет определять точки папоротника,
# которые мы будем отрисовывать

# Объявим массив с нужными нам коэфициентами
Koeficients = [[0, 0, 0, .16, 0, 0],
				 [.85, .04, -.04, .85, 0, 1.6], 
				 [.2, -.26, .23, .22, 0, 1.6],
				 [-.15, .28, .26, .24, 0, .44]]

def f(x, y, a, b, c, d, e, f):
	'''
	Эта функция будет считать новую точку нашего папоротника, 
	по старым координатам x, y и аргуиентам a, b, c, d, e, f 
	'''
	return np.matrix([[a, b], [c, d]]) * np.matrix([[x], [y]]) + np.matrix([[e], [f]])

win = pygame.display.set_mode((600, 600)) # Создадим окно 600х600
pygame.display.set_caption("Barnsley fern") # Опредилим имя окна

x, y = 0, 0 # Изначальные координаты
RUN = True

while RUN:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			RUN = False
			# При нажатии кнопки выход будем закрывать окно

	P = random.randint(0, 100) # Изходя из вероятности будем вычислять новые координаты

	if P == 0:
		XY = f(x, y, *Koeficients[0])
	elif P < 85:
		XY = f(x, y, *Koeficients[1])
	elif P < 93:
		XY = f(x, y, *Koeficients[2])
	else: 
		XY = f(x, y, *Koeficients[3])

	x = XY[0].item()
	y = XY[1].item()

	# Отрисуем точки нашего папаратника
	pygame.draw.line(win, (0, 255, 0), (x * 60 + 300, y * 60), 
                     (x * 60 + 300, y * 60), 1)
	pygame.display.update()

pygame.quit()