# -*- coding: utf-8 *-*
# Множество мандельброта на python
# Использовать будем библиотеку pygame
import pygame # импортируем её
pygame.init() # инициализируем

win = pygame.display.set_mode((600, 600)) # создаем окно 600х600 пикселей

pygame.display.set_caption("Mandelbrot set") # дадим окну имя

# Все работает, но медленно, поэтому вынесем обработку точек за главный цикл,
# он будет только все отрисовавать
for x in range(600):
	for y in range(600):
		i, j = (x - 300) / 150, (y - 300) / 150 # Вещественная и мнимая части числа

		c = (i + j*((-1)**.5))

		In_Mandelbrot = True
		z = 0
		for i in range(50): # Попробуем увеличить максимальное число итераций обработки числа
		# как мы видим, картинка стала четче
		# увеличим сильнее
			z = z**2 + c
			if abs(z) >= 2:
				In_Mandelbrot = False
				break
		color = round(255 * min(abs(c)/2, 1))
		if In_Mandelbrot:
			pygame.draw.line(win, (color, color, color), (x, y), (x, y), 1)

RUN = True
while RUN: # Главный цикл для обработки событий
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			RUN = False # При нажатии кнопки выход выходим из главного цикла
	
	# Отрисуем оси Вещественных и Мнимых чисел
	pygame.draw.line(win, (255, 255, 255), (0, 300), (600, 300), 1) # Real - x
	pygame.draw.line(win, (255, 255, 255), (300, 0), (300, 600), 1) # Imaginary - y

	
	pygame.display.update() # Отрисуем координатную плоскость
	pygame.time.delay(33) # Делаем задержку после отрисовки кадра

pygame.quit()

# Ставьте лайки и подписывайтесь на канал, дальше вас ждет еще много всего интересного
# На 15 лайков под этим видео я выложу этот код и вы сами сможете поиграться с ним
# Пока!
