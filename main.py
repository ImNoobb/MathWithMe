import pygame
from pygame.locals import *
from assets.CND import *

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
def check_quit():
	global running
	for event in pygame.event.get():
		if event.type == QUIT:
			running = False
# Pages Varibles ================================================================= #
start = True
select_class = False

lop6 = False
lop6_Dai_I = False
lop6_Dai_II = False
lop6_Dai_III = False
lop6_Dai_IV = False

lop6_Hinh_I = False
lop6_Hinh_II = False
lop6_Hinh_III = False
lop6_Hinh_IV = False


lop7 = False
lop7_Dai_I = False
lop7_Dai_II = False
lop7_Dai_III = False
lop7_Dai_IV = False

lop7_Hinh_I = False
lop7_Hinh_II = False
lop7_Hinh_III = False
lop7_Hinh_IV = False

lop8 = False
lop8_Dai_I = False
lop8_Dai_II = False
lop8_Dai_III = False
lop8_Dai_IV = False

lop8_Hinh_I = False
lop8_Hinh_II = False
lop8_Hinh_III = False
lop8_Hinh_IV = False

lop9 = False
lop9_Dai_I = False
lop9_Dai_II = False
lop9_Dai_III = False
lop9_Dai_IV = False

lop9_Hinh_I = False
lop9_Hinh_II = False
lop9_Hinh_III = False
lop9_Hinh_IV = False
# Start Buttons ================================================================== #
def start_cmd():
	global start,select_class
	start = False
	select_class = True
	print(1)

s_b_1 = pygame.image.load('assets\\buttons\\start_btn_1.png').convert_alpha()
s_b_2 = pygame.image.load('assets\\buttons\\start_btn_2.png').convert_alpha()
s_b_3 = pygame.image.load('assets\\buttons\\start_btn_3.png').convert_alpha()
s_b_4 = pygame.image.load('assets\\buttons\\start_btn_4.png').convert_alpha()
s_b_5 = pygame.image.load('assets\\buttons\\start_btn_5.png').convert_alpha()
s_b_6 = pygame.image.load('assets\\buttons\\start_btn_6.png').convert_alpha()
start_btn_list = [s_b_1,s_b_2,s_b_3,s_b_4,s_b_5,s_b_6]
start_button = A_Button(start_btn_list,0.5,(540,460),start_cmd)

# Lop 6 Button ==================================================================== #
def lop6_cmd():
	global lop6,select_class
	lop6 = True
	select_class = False

lop6_1 = pygame.image.load('assets\\buttons\\lop6_1.png')
lop6_2 = pygame.image.load('assets\\buttons\\lop6_2.png')
lop6_3 = pygame.image.load('assets\\buttons\\lop6_3.png')
lop6_4 = pygame.image.load('assets\\buttons\\lop6_4.png')
lop6_5 = pygame.image.load('assets\\buttons\\lop6_5.png')
lop6_6 = pygame.image.load('assets\\buttons\\lop6_6.png')
lop6_list = [lop6_1,lop6_2,lop6_3,lop6_4,lop6_5,lop6_6]
lop6_button = A_Button(lop6_list,0.5,(245,180),lop6_cmd)
# BackGrounds ===================================================================== #
start_bg = pygame.image.load('assets\\backgrounds\\start_bg.jpg').convert()
####################
click = False      #
can_c = True       #
def s_m_o_f():     #
	global click   #
	click = False  #
####################
running = True
# ===================================================== #
while running:
	if pygame.mouse.get_pressed()[0] and can_c:
			click = True
			can_c = False
	if start:
		screen.blit(start_bg,(0,0))
		start_button.run(screen,click,s_m_o_f)
	elif select_class:
		screen.fill((255,255,255))
		lop6_button.run(screen,click,s_m_o_f)
	elif lop6:
		screen.fill((255,255,255))
	if pygame.mouse.get_pressed()[0] == False and can_c==False:
			can_c = True
	pygame.display.update()
	clock.tick(60)
	check_quit()

