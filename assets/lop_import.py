import pygame
from pygame.locals import *

lop6_baigiang = []
lop7_baigiang = []
list_temp = []
for i in range(18):
    tempppp = pygame.image.load(f'assets\\baigiang\\lop6\\bai{i+1}.png').convert()
    list_temp.append(tempppp)
lop6_baigiang.append(list_temp)

list_temp = []
for i in range(13):
    tempppp = pygame.image.load(f'assets\\baigiang\\lop6\\bai{i+1}_1.png').convert()
    list_temp.append(tempppp)
lop6_baigiang.append(list_temp)

list_temp = []
for i in range(17):
    tempppp = pygame.image.load(f'assets\\baigiang\\lop6\\bai{i+1}_2.png').convert()
    list_temp.append(tempppp)
lop6_baigiang.append(list_temp)

list_temp = []
for i in range(10):
    tempppp = pygame.image.load(f'assets\\baigiang\\lop6\\bai{i+1}_3.png').convert()
    list_temp.append(tempppp)
lop6_baigiang.append(list_temp)
