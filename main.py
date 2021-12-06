import pygame
from pygame.locals import *
from assets.CND import *

pygame.init()
screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption('MathWithMe!')
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
	lop6_button.set_index(5)
	lop7_button.set_index(5)
	lop8_button.set_index(5)
	lop9_button.set_index(5)
	setting_button.set_index(5)
	start = False
	select_class = True

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

lop6_1 = pygame.image.load('assets\\buttons\\lop6_1.png').convert_alpha()
lop6_2 = pygame.image.load('assets\\buttons\\lop6_2.png').convert_alpha()
lop6_3 = pygame.image.load('assets\\buttons\\lop6_3.png').convert_alpha()
lop6_4 = pygame.image.load('assets\\buttons\\lop6_4.png').convert_alpha()
lop6_5 = pygame.image.load('assets\\buttons\\lop6_5.png').convert_alpha()
lop6_6 = pygame.image.load('assets\\buttons\\lop6_6.png').convert_alpha()
lop6_list = [lop6_1,lop6_2,lop6_3,lop6_4,lop6_5,lop6_6]
lop6_button = A_Button(lop6_list,0.5,(245,180),lop6_cmd)
# Lop 7 Button ==================================================================== #
def lop7_cmd():
	global lop7,select_class
	lop7 = True
	select_class = False

lop7_1 = pygame.image.load('assets\\buttons\\lop7_1.png').convert_alpha()
lop7_2 = pygame.image.load('assets\\buttons\\lop7_2.png').convert_alpha()
lop7_3 = pygame.image.load('assets\\buttons\\lop7_3.png').convert_alpha()
lop7_4 = pygame.image.load('assets\\buttons\\lop7_4.png').convert_alpha()
lop7_5 = pygame.image.load('assets\\buttons\\lop7_5.png').convert_alpha()
lop7_6 = pygame.image.load('assets\\buttons\\lop7_6.png').convert_alpha()
lop7_list = [lop7_1,lop7_2,lop7_3,lop7_4,lop7_5,lop7_6]
lop7_button = A_Button(lop7_list,0.5,(470,180),lop7_cmd)
# Lop 8 Button ==================================================================== #
def lop8_cmd():
	global lop8,select_class
	lop8 = True
	select_class = False

lop8_1 = pygame.image.load('assets\\buttons\\lop8_1.png').convert_alpha()
lop8_2 = pygame.image.load('assets\\buttons\\lop8_2.png').convert_alpha()
lop8_3 = pygame.image.load('assets\\buttons\\lop8_3.png').convert_alpha()
lop8_4 = pygame.image.load('assets\\buttons\\lop8_4.png').convert_alpha()
lop8_5 = pygame.image.load('assets\\buttons\\lop8_5.png').convert_alpha()
lop8_6 = pygame.image.load('assets\\buttons\\lop8_6.png').convert_alpha()
lop8_list = [lop8_1,lop8_2,lop8_3,lop8_4,lop8_5,lop8_6]
lop8_button = A_Button(lop8_list,0.5,(695,180),lop8_cmd)
# Lop 9 Button ==================================================================== #
def lop9_cmd():
	global lop9,select_class
	lop9 = True
	select_class = False

lop9_1 = pygame.image.load('assets\\buttons\\lop9_1.png').convert_alpha()
lop9_2 = pygame.image.load('assets\\buttons\\lop9_2.png').convert_alpha()
lop9_3 = pygame.image.load('assets\\buttons\\lop9_3.png').convert_alpha()
lop9_4 = pygame.image.load('assets\\buttons\\lop9_4.png').convert_alpha()
lop9_5 = pygame.image.load('assets\\buttons\\lop9_5.png').convert_alpha()
lop9_6 = pygame.image.load('assets\\buttons\\lop9_6.png').convert_alpha()
lop9_list = [lop9_1,lop9_2,lop9_3,lop9_4,lop9_5,lop9_6]
lop9_button = A_Button(lop9_list,0.5,(920,180),lop9_cmd)
# Back Button ===================================================================== #
def back_now(s1,s2):
	global select_class,start,lop6,lop7,lop8,lop9,setting
	if s1 == 'select_class':
		select_class = True
	elif s1 == 'start':
		start = True

	if s2 == 'select_class':
		select_class = False
	elif s2 == 'lop6':
		lop6 = False
	elif s2 == 'lop7':
		lop7 = False
	elif s2 == 'lop8':
		lop8 = False
	elif s2 == 'lop9':
		lop9 = False
	elif s2 == 'setting':
		setting = False

back1 = pygame.image.load('assets\\buttons\\back_button_1.png').convert_alpha()
back2 = pygame.image.load('assets\\buttons\\back_button_2.png').convert_alpha()
back_button_to_start = N_Button(back1,back2,(0,0),lambda: back_now('start','select_class'))
back_button_to_sc = N_Button(back1,back2,(0,0),lambda: back_now('select_class','setting'))

back_button_to_sc6 = N_Button(back1,back2,(0,0),lambda: back_now('select_class','lop6'))
back_button_to_sc7 = N_Button(back1,back2,(0,0),lambda: back_now('select_class','lop7'))
back_button_to_sc8 = N_Button(back1,back2,(0,0),lambda: back_now('select_class','lop8'))
back_button_to_sc9 = N_Button(back1,back2,(0,0),lambda: back_now('select_class','lop9'))
# Settings Button ================================================================= #
def settings_cmd():
	global setting,select_class
	select_class = False
	setting = True

setting_1 = pygame.image.load('assets\\buttons\\settings_1.png').convert_alpha()
setting_2 = pygame.image.load('assets\\buttons\\settings_2.png').convert_alpha()
setting_3 = pygame.image.load('assets\\buttons\\settings_3.png').convert_alpha()
setting_4 = pygame.image.load('assets\\buttons\\settings_4.png').convert_alpha()
setting_5 = pygame.image.load('assets\\buttons\\settings_5.png').convert_alpha()
setting_6 = pygame.image.load('assets\\buttons\\settings_6.png').convert_alpha()

setting_list = [setting_1,setting_2,setting_3,setting_4,setting_5,setting_6]
setting_button = A_Button(setting_list,0.5,(1280-205,720-155),settings_cmd)
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
#pygame.mouse.set_pos((1280/2,720/2))
font = pygame.font.Font('assets\\arial.TTF',20)
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
		lop7_button.run(screen,click,s_m_o_f)
		lop8_button.run(screen,click,s_m_o_f)
		lop9_button.run(screen,click,s_m_o_f)
		back_button_to_start.run(screen,click,s_m_o_f)
		setting_button.run(screen,click,s_m_o_f)

		if lop6_button.get_collide():
			show_label(screen,'Học chương trình lớp 6',font,(0,0,0),(1280/2,700))
		if lop7_button.get_collide():
			show_label(screen,'Học chương trình lớp 7',font,(0,0,0),(1280/2,700))
		if lop8_button.get_collide():
			show_label(screen,'Học chương trình lớp 8',font,(0,0,0),(1280/2,700))
		if lop9_button.get_collide():
			show_label(screen,'Học chương trình lớp 9',font,(0,0,0),(1280/2,700))
	elif lop6:
		if lop6_Dai_I:
			pass
		elif lop6_Dai_II:
			pass
		elif lop6_Dai_III:
			pass
		elif lop6_Dai_IV:
			pass
		elif lop6_Hinh_I:
			pass
		elif lop6_Hinh_II:
			pass
		elif lop6_Hinh_III:
			pass
		elif lop6_Hinh_IV:
			pass
		else:
			screen.fill((255,255,255))
			back_button_to_sc6.run(screen,click,s_m_o_f)
	elif lop7:
		if lop7_Dai_I:
			pass
		elif lop7_Dai_II:
			pass
		elif lop7_Dai_III:
			pass
		elif lop7_Dai_IV:
			pass
		elif lop7_Hinh_I:
			pass
		elif lop7_Hinh_II:
			pass
		elif lop7_Hinh_III:
			pass
		elif lop7_Hinh_IV:
			pass
		else:
			screen.fill((255,255,255))
			back_button_to_sc7.run(screen,click,s_m_o_f)
	elif lop8:
		if lop8_Dai_I:
			pass
		elif lop8_Dai_II:
			pass
		elif lop8_Dai_III:
			pass
		elif lop8_Dai_IV:
			pass
		elif lop8_Hinh_I:
			pass
		elif lop8_Hinh_II:
			pass
		elif lop8_Hinh_III:
			pass
		elif lop8_Hinh_IV:
			pass
		else:
			screen.fill((255,255,255))
			back_button_to_sc8.run(screen,click,s_m_o_f)
	elif lop9:
		if lop9_Dai_I:
			pass
		elif lop9_Dai_II:
			pass
		elif lop9_Dai_III:
			pass
		elif lop9_Dai_IV:
			pass
		elif lop9_Hinh_I:
			pass
		elif lop9_Hinh_II:
			pass
		elif lop9_Hinh_III:
			pass
		elif lop9_Hinh_IV:
			pass
		else:
			screen.fill((255,255,255))
			back_button_to_sc9.run(screen,click,s_m_o_f)
	elif setting:
		screen.fill((255,255,255))
		back_button_to_sc.run(screen,click,s_m_o_f)






	if pygame.mouse.get_pressed()[0] == False and can_c==False:
			can_c = True
	pygame.display.update()
	clock.tick(60)
	check_quit()

