import pygame,random,time
from pygame.locals import *


pygame.init()
screen = pygame.display.set_mode((1280,680))#,pygame.NOFRAME)
load_scr = pygame.image.load('assets\\backgrounds\\load_scr.png').convert()
screen.blit(load_scr,(0,0))

pygame.display.set_caption('MathWithMe!')
icon = pygame.image.load('assets\\icon.png')
pygame.display.set_icon(icon)
pygame.display.update()
clock = pygame.time.Clock()
scroll_y  = 0
from assets.lop_import import *
from assets.CND import *
def check_quit():
	global running,scroll_y
	for event in pygame.event.get():
		if event.type == QUIT:
			running = False
			return True
		if event.type == MOUSEBUTTONDOWN:
			if event.button ==4:
				scroll_y += 30
			elif event.button == 5:
				scroll_y -= 30

# Pages Varibles ================================================================= #
start = True
select_class = False

XO_l6 = False
lop6 = False
lop6_Dai_I = False
lop6_Dai_II = False
lop6_Dai_III = False

lop6_Hinh_I = False
lop6_Hinh_II = False


CM_l7 = True
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
# Tile Bar Button =============================================================== #
def close_func():
	global running
	running = False

def minimize_func():
	pygame.display.iconify()

close_img = pygame.image.load('assets\\buttons\\X_Button.png').convert_alpha()
close_img_1 = pygame.image.load('assets\\buttons\\X_Button_2.png').convert_alpha()
minimize_img = pygame.image.load('assets\\buttons\\minimize.png').convert_alpha()
minimize_img_1 = pygame.image.load('assets\\buttons\\minimize_2.png').convert_alpha()
close_button = N_Button(close_img,close_img_1,(1238,2),close_func)
minimize_button = N_Button(minimize_img,minimize_img_1,(1188,2),minimize_func)
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
	Chuong_I_Dai_Button.change_cmd(lambda:Chuong_I_cmd(6,'dai'))
	Chuong_I_Hinh_Button.change_cmd(lambda: Chuong_I_cmd(6,'hinh'))
	Chuong_II_Dai_Button.change_cmd(lambda:Chuong_II_cmd(6,'dai'))
	Chuong_II_Hinh_Button.change_cmd(lambda: Chuong_II_cmd(6,'hinh'))
	Chuong_III_Dai_Button.change_cmd(lambda:Chuong_III_cmd(6,'dai'))


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
	Chuong_I_Dai_Button.change_cmd(lambda:Chuong_I_cmd(7,'dai'))
	Chuong_I_Hinh_Button.change_cmd(lambda: Chuong_I_cmd(7,'hinh'))
	Chuong_II_Dai_Button.change_cmd(lambda:Chuong_II_cmd(7,'dai'))
	Chuong_II_Hinh_Button.change_cmd(lambda: Chuong_II_cmd(7,'hinh'))
	Chuong_III_Dai_Button.change_cmd(lambda:Chuong_III_cmd(7,'dai'))
	Chuong_III_Hinh_Button.change_cmd(lambda: Chuong_III_cmd(7,'hinh'))
	Chuong_IV_Dai_Button.change_cmd(lambda:Chuong_IV_cmd(7,'dai'))


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
	Chuong_I_Dai_Button.change_cmd(lambda:Chuong_I_cmd(8,'dai'))
	Chuong_I_Hinh_Button.change_cmd(lambda: Chuong_I_cmd(8,'hinh'))
	Chuong_II_Dai_Button.change_cmd(lambda:Chuong_II_cmd(8,'dai'))
	Chuong_II_Hinh_Button.change_cmd(lambda: Chuong_II_cmd(8,'hinh'))
	Chuong_III_Dai_Button.change_cmd(lambda:Chuong_III_cmd(8,'dai'))
	Chuong_III_Hinh_Button.change_cmd(lambda: Chuong_III_cmd(8,'hinh'))
	Chuong_IV_Dai_Button.change_cmd(lambda:Chuong_IV_cmd(8,'dai'))
	Chuong_IV_Hinh_Button.change_cmd(lambda: Chuong_IV_cmd(8,'hinh'))

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
	Chuong_I_Dai_Button.change_cmd(lambda:Chuong_I_cmd(9,'dai'))
	Chuong_I_Hinh_Button.change_cmd(lambda: Chuong_I_cmd(9,'hinh'))
	Chuong_II_Dai_Button.change_cmd(lambda:Chuong_II_cmd(9,'dai'))
	Chuong_II_Hinh_Button.change_cmd(lambda: Chuong_II_cmd(9,'hinh'))
	Chuong_III_Dai_Button.change_cmd(lambda:Chuong_II_cmd(9,'dai'))
	Chuong_III_Hinh_Button.change_cmd(lambda: Chuong_II_cmd(9,'hinh'))
	Chuong_IV_Dai_Button.change_cmd(lambda:Chuong_II_cmd(9,'dai'))
	Chuong_IV_Hinh_Button.change_cmd(lambda: Chuong_II_cmd(9,'hinh'))

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
# Chuong I Button ================================================================= #
def Chuong_I_cmd(lop,which):
	global lop6_Dai_I,lop7_Dai_I,lop8_Dai_I,lop9_Dai_I,lop6_Hinh_I,lop7_Hinh_I,lop8_Hinh_I,lop9_Hinh_I,lop6,lop7,lop8,lop9
	if which == 'dai':
		if lop == 6:
			lop6_Dai_I = True
		elif lop == 7:
			lop7_Dai_I = True
		elif lop == 8:
			lop8_Dai_I = True
		elif lop == 9:
			lop9_Dai_I = True
	elif which == 'hinh':
		if lop == 6:
			lop6_Hinh_I = True
		elif lop == 7:
			lop7_Hinh_I = True
		elif lop == 8:
			lop8_Hinh_I = True
		elif lop == 9:
			lop9_Hinh_I = True


chuong_I_1 = pygame.image.load('assets\\buttons\\chuong_I_1.png').convert_alpha()
chuong_I_2 = pygame.image.load('assets\\buttons\\chuong_I_2.png').convert_alpha()

Chuong_I_Dai_Button = N_Button(chuong_I_1,chuong_I_2,(76,252),lambda: Chuong_I_cmd(6,'dai'))
Chuong_I_Hinh_Button = N_Button(chuong_I_1,chuong_I_2,(82,497),lambda: Chuong_I_cmd(6,'hinh'))
# Chuong II Button ================================================================= #
def Chuong_II_cmd(lop,which):
	global lop6_Dai_II,lop7_Dai_II,lop8_Dai_II,lop9_Dai_II,lop6_Hinh_II,lop7_Hinh_II,lop8_Hinh_II,lop9_Hinh_II,lop6,lop7,lop8,lop9
	if which == 'dai':
		if lop == 6:
			lop6_Dai_II = True
		elif lop == 7:
			lop7_Dai_II = True
		elif lop == 8:
			lop8_Dai_II = True
		elif lop == 9:
			lop9_Dai_II = True
	elif which == 'hinh':
		if lop == 6:
			lop6_Hinh_II = True
		elif lop == 7:
			lop7_Hinh_II = True
		elif lop == 8:
			lop8_Hinh_II = True
		elif lop == 9:
			lop9_Hinh_II = True


chuong_II_1 = pygame.image.load('assets\\buttons\\chuong_II_1.png').convert_alpha()
chuong_II_2 = pygame.image.load('assets\\buttons\\chuong_II_2.png').convert_alpha()

Chuong_II_Dai_Button = N_Button(chuong_II_1,chuong_II_2,(238,252),lambda: Chuong_II_cmd(6,'dai'))
Chuong_II_Hinh_Button = N_Button(chuong_II_1,chuong_II_2,(243,497),lambda: Chuong_II_cmd(6,'hinh'))
# Chuong III Button ================================================================= #
def Chuong_III_cmd(lop,which):
	global lop6_Dai_III,lop7_Dai_III,lop8_Dai_III,lop9_Dai_III,lop6_Hinh_III,lop7_Hinh_III,lop8_Hinh_III,lop9_Hinh_III,lop6,lop7,lop8,lop9
	if which == 'dai':
		if lop == 6:
			lop6_Dai_III = True
		elif lop == 7:
			lop7_Dai_III = True
		elif lop == 8:
			lop8_Dai_III = True
		elif lop == 9:
			lop9_Dai_III = True
	elif which == 'hinh':
		if lop == 6:
			lop6_Hinh_III = True
		elif lop == 7:
			lop7_Hinh_III = True
		elif lop == 8:
			lop8_Hinh_III = True
		elif lop == 9:
			lop9_Hinh_III = True


chuong_III_1 = pygame.image.load('assets\\buttons\\chuong_III_1.png').convert_alpha()
chuong_III_2 = pygame.image.load('assets\\buttons\\chuong_III_2.png').convert_alpha()

Chuong_III_Dai_Button = N_Button(chuong_III_1,chuong_III_2,(76,317),lambda: Chuong_III_cmd(6,'dai'))
Chuong_III_Hinh_Button = N_Button(chuong_III_1,chuong_III_2,(81,560),lambda: Chuong_III_cmd(6,'hinh'))
# Chuong IV Button ================================================================= #
def Chuong_IV_cmd(lop,which):
	global lop6_Dai_IV,lop7_Dai_IV,lop8_Dai_IV,lop9_Dai_IV,lop6_Hinh_IV,lop7_Hinh_IV,lop8_Hinh_IV,lop9_Hinh_IV,lop6,lop7,lop8,lop9
	if which == 'dai':
		if lop == 6:
			lop6_Dai_IV = True
		elif lop == 7:
			lop7_Dai_IV = True
		elif lop == 8:
			lop8_Dai_IV = True
		elif lop == 9:
			lop9_Dai_IV = True
	elif which == 'hinh':
		if lop == 6:
			lop6_Hinh_IV = True
		elif lop == 7:
			lop7_Hinh_IV = True
		elif lop == 8:
			lop8_Hinh_IV = True
		elif lop == 9:
			lop9_Hinh_IV = True


chuong_IV_1 = pygame.image.load('assets\\buttons\\chuong_IV_1.png').convert_alpha()
chuong_IV_2 = pygame.image.load('assets\\buttons\\chuong_IV_2.png').convert_alpha()

Chuong_IV_Dai_Button = N_Button(chuong_IV_1,chuong_IV_2,(238,317),lambda: Chuong_IV_cmd(6,'dai'))
Chuong_IV_Hinh_Button = N_Button(chuong_IV_1,chuong_IV_2,(243,560),lambda: Chuong_IV_cmd(6,'hinh'))

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
setting_button = A_Button(setting_list,0.5,(1280-205,500),settings_cmd)
# Back to lop 6 =================================================================== #
def back_6():
	global lop6,lop6_Dai_I,lop6_Dai_II,lop6_Dai_III,lop6_Hinh_I,lop6_Hinh_II,XO_l6
	lop6_Dai_I = False
	lop6_Dai_II = False
	lop6_Dai_III = False
	lop6_Hinh_I = False
	lop6_Hinh_II = False
back_button_to_l6 = N_Button(back1,back2,(0,0),back_6)

def back___():
	global baigiang_running
	baigiang_running = False
back_to_class = N_Button(back1, back2, (0,0), back___)

class_button_img = []
for i in range(19):
	temp = pygame.image.load(f'assets\\buttons\\bai{i+1}_1.png').convert_alpha()
	temp2 = pygame.image.load(f'assets\\buttons\\bai{i+1}_2.png').convert_alpha()
	class_button_img.append([temp,temp2])

# Bai 6 Buttons === #
def l6_screen_display_dai(bai,y):
	global scroll_y,running,baigiang_running
	screen.fill((255,255,255))
	if 720-lop6_baigiang[y][bai].get_height()>0:
		scroll_y = 0
	elif scroll_y>0:
		scroll_y = 0
	elif scroll_y<680-lop6_baigiang[y][bai].get_height():
		scroll_y = 680-lop6_baigiang[y][bai].get_height()
	screen.blit(lop6_baigiang[y][bai],(200,scroll_y))
	back_to_class.run(screen,click,s_m_o_f)
	show_label(screen, 'Bản quyền thuộc về Bộ GD và ĐT', font, (255,0,0), (1100,660))
	pygame.display.update()
	clock.tick(60)
	for event in pygame.event.get():
		if event.type == MOUSEBUTTONDOWN:
			if event.button == 4:
				scroll_y += 40
			elif event.button == 5:
				scroll_y -= 40
		if event.type == QUIT:
			quit()

def lop6_bai(bai,chuong):
	global scroll_y,running,baigiang_running
	baigiang_running = True
	if chuong == 'daiI':
		scroll_y = 0
		while baigiang_running:
			l6_screen_display_dai(bai,0)
	elif chuong == 'daiII':
		scroll_y = 0
		while baigiang_running:
			l6_screen_display_dai(bai,1)
	elif chuong == 'daiIII':
		scroll_y = 0
		while baigiang_running:
			l6_screen_display_dai(bai,2)
	elif chuong == 'hinhI':
		scroll_y = 0
		while baigiang_running:
			l6_screen_display_dai(bai,3)
	elif chuong == 'hinhII':
		scroll_y = 0
		while baigiang_running:
			l6_screen_display_dai(bai,4)
		

				

lop6_buttons_Dai_I = []
for i in range(1,19):
	if i<=5:
		posX = 100+(i-1)*230
		posY = 100
	elif i<=10:
		posX = 100+(i-6)*230
		posY = 225
	elif i<=15:
		posX = 100+(i-11)*230
		posY = 350
	else:
		posX = 100+(i-16)*230
		posY = 475

	temp = N_Button(class_button_img[i-1][0],class_button_img[i-1][1],(posX,posY),lambda: lop6_bai(i,'daiI'))
	lop6_buttons_Dai_I.append(temp)


lop6_buttons_Dai_II = []
for i in range(1,14):
	if i<=5:
		posX = 100+(i-1)*230
		posY = 100
	elif i<=10:
		posX = 100+(i-6)*230
		posY = 225
	elif i<=15:
		posX = 100+(i-11)*230
		posY = 350
	else:
		posX = 100+(i-16)*230
		posY = 475

	temp = N_Button(class_button_img[i-1][0],class_button_img[i-1][1],(posX,posY),lambda: lop6_bai(i,'daiII'))
	lop6_buttons_Dai_II.append(temp)


lop6_buttons_Dai_III = []
for i in range(1,18):
	if i<=5:
		posX = 100+(i-1)*230
		posY = 100
	elif i<=10:
		posX = 100+(i-6)*230
		posY = 225
	elif i<=15:
		posX = 100+(i-11)*230
		posY = 350
	else:
		posX = 100+(i-16)*230
		posY = 475

	temp = N_Button(class_button_img[i-1][0],class_button_img[i-1][1],(posX,posY),lambda: lop6_bai(i,'daiIII'))
	lop6_buttons_Dai_III.append(temp)


lop6_buttons_Hinh_I = []
for i in range(1,11):
	if i<=5:
		posX = 100+(i-1)*230
		posY = 100
	elif i<=10:
		posX = 100+(i-6)*230
		posY = 225
	elif i<=15:
		posX = 100+(i-11)*230
		posY = 350
	else:
		posX = 100+(i-16)*230
		posY = 475

	temp = N_Button(class_button_img[i-1][0],class_button_img[i-1][1],(posX,posY),lambda: lop6_bai(i,'hinhI'))
	lop6_buttons_Hinh_I.append(temp)

lop6_buttons_Hinh_II = []
for i in range(1,10):
	if i<=5:
		posX = 100+(i-1)*230
		posY = 100
	elif i<=10:
		posX = 100+(i-6)*230
		posY = 225
	elif i<=15:
		posX = 100+(i-11)*230
		posY = 350
	else:
		posX = 100+(i-16)*230
		posY = 475

	temp = N_Button(class_button_img[i-1][0],class_button_img[i-1][1],(posX,posY),lambda: lop6_bai(i,'hinhII'))
	lop6_buttons_Hinh_II.append(temp)
# Back to lop 7 =================================================================== #
def back_7():
	global lop7,lop7_Dai_I,lop7_Dai_II,lop7_Dai_III,lop7_Dai_IV,lop7_Hinh_I,lop7_Hinh_II,lop7_Hinh_III
	lop7_Dai_I = False
	lop7_Dai_II = False
	lop7_Dai_III = False
	lop7_Dai_IV = False
	lop7_Hinh_I = False
	lop7_Hinh_II = False
	lop7_Hinh_III = False
back_button_to_l7 = N_Button(back1,back2,(0,0),back_7)


# Bai 7 Buttons === #
def l7_screen_display_dai_I(bai,y):
	global scroll_y,running,baigiang_running
	screen.fill((255,255,255))
	if 680-lop7_baigiang[y][bai].get_height()>0:
		scroll_y = 0
	elif scroll_y>0:
		scroll_y = 0
	elif scroll_y<680-lop7_baigiang[y][bai].get_height():
		scroll_y = 680-lop7_baigiang[y][bai].get_height()
	screen.blit(lop7_baigiang[y][bai],(200,scroll_y))
	back_to_class.run(screen,click,s_m_o_f)
	show_label(screen, 'Bản quyền thuộc về Bộ GD và ĐT', font, (255,0,0), (1100,640))
	pygame.display.update()
	clock.tick(60)
	for event in pygame.event.get():
		if event.type == MOUSEBUTTONDOWN:
			if event.button == 4:
				scroll_y += 40
			elif event.button == 5:
				scroll_y -= 40
		if event.type == QUIT:
			quit()

def lop7_bai(bai,chuong):
	global scroll_y,running,baigiang_running
	baigiang_running = True
	if chuong == 'daiI':
		scroll_y = 0
		while baigiang_running:
			l7_screen_display_dai_I(bai,0)
	elif chuong == 'daiII':
		scroll_y = 0
		while baigiang_running:
			l7_screen_display_dai_I(bai,1)
	elif chuong == 'daiIII':
		scroll_y = 0
		while baigiang_running:
			l7_screen_display_dai_I(bai,2)
	elif chuong == 'daiIV':
		scroll_y = 0
		while baigiang_running:
			l7_screen_display_dai_I(bai,3)
	elif chuong == 'hinhI':
		scroll_y = 0
		while baigiang_running:
			l7_screen_display_dai_I(bai,4)
	elif chuong == 'hinhII':
		scroll_y = 0
		while baigiang_running:
			l7_screen_display_dai_I(bai,5)
	elif chuong == 'hinhIII':
		scroll_y = 0
		while baigiang_running:
			l7_screen_display_dai_I(bai,6)

				

lop7_buttons_Dai_I = []
for i in range(1,13):
	if i<=5:
		posX = 100+(i-1)*230
		posY = 100
	elif i<=10:
		posX = 100+(i-7)*230
		posY = 225
	elif i<=15:
		posX = 100+(i-11)*230
		posY = 350
	else:
		posX = 100+(i-17)*230
		posY = 475

	temp = N_Button(class_button_img[i-1][0],class_button_img[i-1][1],(posX,posY),lambda: lop7_bai(i,'daiI'))
	lop7_buttons_Dai_I.append(temp)


lop7_buttons_Dai_II = []
for i in range(1,8):
	if i<=5:
		posX = 100+(i-1)*230
		posY = 100
	elif i<=10:
		posX = 100+(i-7)*230
		posY = 225
	elif i<=15:
		posX = 100+(i-11)*230
		posY = 350
	else:
		posX = 100+(i-17)*230
		posY = 475

	temp = N_Button(class_button_img[i-1][0],class_button_img[i-1][1],(posX,posY),lambda: lop7_bai(i,'daiII'))
	lop7_buttons_Dai_II.append(temp)


lop7_buttons_Dai_III = []
for i in range(1,5):
	if i<=5:
		posX = 100+(i-1)*230
		posY = 100
	elif i<=10:
		posX = 100+(i-7)*230
		posY = 225
	elif i<=15:
		posX = 100+(i-11)*230
		posY = 350
	else:
		posX = 100+(i-17)*230
		posY = 475

	temp = N_Button(class_button_img[i-1][0],class_button_img[i-1][1],(posX,posY),lambda: lop7_bai(i,'daiIII'))
	lop7_buttons_Dai_III.append(temp)

lop7_buttons_Dai_IV = []
for i in range(1,10):
	if i<=5:
		posX = 100+(i-1)*230
		posY = 100
	elif i<=10:
		posX = 100+(i-7)*230
		posY = 225
	elif i<=15:
		posX = 100+(i-11)*230
		posY = 350
	else:
		posX = 100+(i-17)*230
		posY = 475

	temp = N_Button(class_button_img[i-1][0],class_button_img[i-1][1],(posX,posY),lambda: lop7_bai(i,'daiIV'))
	lop7_buttons_Dai_IV.append(temp)


lop7_buttons_Hinh_I = []
for i in range(1,8):
	if i<=5:
		posX = 100+(i-1)*230
		posY = 100
	elif i<=10:
		posX = 100+(i-7)*230
		posY = 225
	elif i<=15:
		posX = 100+(i-11)*230
		posY = 350
	else:
		posX = 100+(i-17)*230
		posY = 475

	temp = N_Button(class_button_img[i-1][0],class_button_img[i-1][1],(posX,posY),lambda: lop7_bai(i,'hinhI'))
	lop7_buttons_Hinh_I.append(temp)

lop7_buttons_Hinh_II = []
for i in range(1,10):
	if i<=5:
		posX = 100+(i-1)*230
		posY = 100
	elif i<=10:
		posX = 100+(i-7)*230
		posY = 225
	elif i<=15:
		posX = 100+(i-11)*230
		posY = 350
	else:
		posX = 100+(i-17)*230
		posY = 475

	temp = N_Button(class_button_img[i-1][0],class_button_img[i-1][1],(posX,posY),lambda: lop7_bai(i,'hinhII'))
	lop7_buttons_Hinh_II.append(temp)

lop7_buttons_Hinh_III = []
for i in range(1,10):
	if i<=5:
		posX = 100+(i-1)*230
		posY = 100
	elif i<=10:
		posX = 100+(i-7)*230
		posY = 225
	elif i<=15:
		posX = 100+(i-11)*230
		posY = 350
	else:
		posX = 100+(i-17)*230
		posY = 475

	temp = N_Button(class_button_img[i-1][0],class_button_img[i-1][1],(posX,posY),lambda: lop7_bai(i,'hinhIII'))
	lop7_buttons_Hinh_III.append(temp)

# Bai 8 Buttons === #
def back_8():
	global lop7,lop8_Dai_I,lop8_Dai_II,lop8_Dai_III,lop8_Dai_IV,lop8_Hinh_I,lop8_Hinh_II,lop8_Hinh_III,lop8_Hinh_IV
	lop8_Dai_I = False
	lop8_Dai_II = False
	lop8_Dai_III = False
	lop8_Dai_IV = False
	lop8_Hinh_I = False
	lop8_Hinh_II = False
	lop8_Hinh_III = False
	lop8_Hinh_IV = False
back_button_to_l8 = N_Button(back1,back2,(0,0),back_8)

def l8_screen_display_dai_I(bai,y):
	global scroll_y,running,baigiang_running
	screen.fill((255,255,255))
	if 680-lop8_baigiang[y][bai].get_height()>0:
		scroll_y = 0
	elif scroll_y>0:
		scroll_y = 0
	elif scroll_y<680-lop8_baigiang[y][bai].get_height():
		scroll_y = 680-lop8_baigiang[y][bai].get_height()
	screen.blit(lop8_baigiang[y][bai],(200,scroll_y))
	back_to_class.run(screen,click,s_m_o_f)
	show_label(screen, 'Bản quyền thuộc về Bộ GD và ĐT', font, (255,0,0), (1100,640))
	pygame.display.update()
	clock.tick(60)
	for event in pygame.event.get():
		if event.type == MOUSEBUTTONDOWN:
			if event.button == 4:
				scroll_y += 40
			elif event.button == 5:
				scroll_y -= 40
		if event.type == QUIT:
			quit()

def lop8_bai(bai,chuong):
	global scroll_y,running,baigiang_running
	baigiang_running = True
	if chuong == 'daiI':
		scroll_y = 0
		while baigiang_running:
			l8_screen_display_dai_I(bai,0)
	elif chuong == 'daiII':
		scroll_y = 0
		while baigiang_running:
			l8_screen_display_dai_I(bai,1)
	elif chuong == 'daiIII':
		scroll_y = 0
		while baigiang_running:
			l8_screen_display_dai_I(bai,2)
	elif chuong == 'daiIV':
		scroll_y = 0
		while baigiang_running:
			l8_screen_display_dai_I(bai,3)
	elif chuong == 'hinhI':
		scroll_y = 0
		while baigiang_running:
			l8_screen_display_dai_I(bai,4)
	elif chuong == 'hinhII':
		scroll_y = 0
		while baigiang_running:
			l8_screen_display_dai_I(bai,5)
	elif chuong == 'hinhIII':
		scroll_y = 0
		while baigiang_running:
			l8_screen_display_dai_I(bai,6)

				

lop8_buttons_Dai_I = []
for i in range(1,10):
	if i<=5:
		posX = 100+(i-1)*230
		posY = 100
	elif i<=10:
		posX = 100+(i-7)*230
		posY = 225
	elif i<=15:
		posX = 100+(i-11)*230
		posY = 350
	else:
		posX = 100+(i-17)*230
		posY = 475

	temp = N_Button(class_button_img[i-1][0],class_button_img[i-1][1],(posX,posY),lambda: lop8_bai(i,'daiI'))
	lop8_buttons_Dai_I.append(temp)


lop8_buttons_Dai_II = []
for i in range(1,10):
	if i<=5:
		posX = 100+(i-1)*230
		posY = 100
	elif i<=10:
		posX = 100+(i-7)*230
		posY = 225
	elif i<=15:
		posX = 100+(i-11)*230
		posY = 350
	else:
		posX = 100+(i-17)*230
		posY = 475

	temp = N_Button(class_button_img[i-1][0],class_button_img[i-1][1],(posX,posY),lambda: lop8_bai(i,'daiII'))
	lop8_buttons_Dai_II.append(temp)


lop8_buttons_Dai_III = []
for i in range(1,8):
	if i<=5:
		posX = 100+(i-1)*230
		posY = 100
	elif i<=10:
		posX = 100+(i-7)*230
		posY = 225
	elif i<=15:
		posX = 100+(i-11)*230
		posY = 350
	else:
		posX = 100+(i-17)*230
		posY = 475

	temp = N_Button(class_button_img[i-1][0],class_button_img[i-1][1],(posX,posY),lambda: lop8_bai(i,'daiIII'))
	lop8_buttons_Dai_III.append(temp)

lop8_buttons_Dai_IV = []
for i in range(1,6):
	if i<=5:
		posX = 100+(i-1)*230
		posY = 100
	elif i<=10:
		posX = 100+(i-7)*230
		posY = 225
	elif i<=15:
		posX = 100+(i-11)*230
		posY = 350
	else:
		posX = 100+(i-17)*230
		posY = 475

	temp = N_Button(class_button_img[i-1][0],class_button_img[i-1][1],(posX,posY),lambda: lop8_bai(i,'daiIV'))
	lop8_buttons_Dai_IV.append(temp)


lop8_buttons_Hinh_I = []
for i in range(1,13):
	if i<=5:
		posX = 100+(i-1)*230
		posY = 100
	elif i<=10:
		posX = 100+(i-7)*230
		posY = 225
	elif i<=15:
		posX = 100+(i-11)*230
		posY = 350
	else:
		posX = 100+(i-17)*230
		posY = 475

	temp = N_Button(class_button_img[i-1][0],class_button_img[i-1][1],(posX,posY),lambda: lop8_bai(i,'hinhI'))
	lop8_buttons_Hinh_I.append(temp)

lop8_buttons_Hinh_II = []
for i in range(1,7):
	if i<=5:
		posX = 100+(i-1)*230
		posY = 100
	elif i<=10:
		posX = 100+(i-7)*230
		posY = 225
	elif i<=15:
		posX = 100+(i-11)*230
		posY = 350
	else:
		posX = 100+(i-17)*230
		posY = 475

	temp = N_Button(class_button_img[i-1][0],class_button_img[i-1][1],(posX,posY),lambda: lop8_bai(i,'hinhII'))
	lop8_buttons_Hinh_II.append(temp)

lop8_buttons_Hinh_III = []
for i in range(1,10):
	if i<=5:
		posX = 100+(i-1)*230
		posY = 100
	elif i<=10:
		posX = 100+(i-7)*230
		posY = 225
	elif i<=15:
		posX = 100+(i-11)*230
		posY = 350
	else:
		posX = 100+(i-17)*230
		posY = 475

	temp = N_Button(class_button_img[i-1][0],class_button_img[i-1][1],(posX,posY),lambda: lop8_bai(i,'hinhIII'))
	lop8_buttons_Hinh_III.append(temp)

lop8_buttons_Hinh_IV = []
for i in range(1,10):
	if i<=5:
		posX = 100+(i-1)*230
		posY = 100
	elif i<=10:
		posX = 100+(i-7)*230
		posY = 225
	elif i<=15:
		posX = 100+(i-11)*230
		posY = 350
	else:
		posX = 100+(i-17)*230
		posY = 475

	temp = N_Button(class_button_img[i-1][0],class_button_img[i-1][1],(posX,posY),lambda: lop8_bai(i,'hinhIV'))
	lop8_buttons_Hinh_IV.append(temp)

# X O Games Lop6 Button ========== #
def start_l6():
	global XO_l6
	XO_l6 = True
temp1 = pygame.image.load('assets\\buttons\\toanXO_1.png').convert_alpha()
temp2 = pygame.image.load('assets\\buttons\\toanXO_2.png').convert_alpha()
X_O_game6 = N_Button(temp1,temp2,(782,282),start_l6)
# =============================================#
temp1 = pygame.image.load('assets\\buttons\\replay_button.png').convert_alpha()
temp2 = pygame.image.load('assets\\buttons\\replay_button_1.png').convert_alpha()
XO_replay = False
def replay():
	global XO_replay
	XO_replay = True
XO_replay_button = N_Button(temp1,temp2,(566,580),replay)
def back_XO():
	global XO_l6,XO_selected,XO_running,XO_wait,XO_O,XO_turn,XO_x1,XO_x2,XO_ans,XO_q_ans,XO_question,XO_win,XO_lose,XO_index,XO_RAP,XO_AnsButton,XO_a,XO_a_pos,XO_OK,XO_pos,XO_replay,XO_text
	XO_l6 = False
	XO_font = pygame.font.Font(None,25)
	XO_selected = None
	XO_wait = False
	XO_running = True
	XO_wait = True
	XO_O = ['n','n','n','n','n','n','n','n','n']
	XO_turn = 'p'
	XO_bg = pygame.image.load('assets\\backgrounds\\X_O_bg.png').convert()
	temp1 = pygame.image.load('assets\\buttons\\X_O_button.png').convert()
	temp2 = pygame.image.load('assets\\buttons\\X_O_button_1.png').convert()
	XO_button = [temp1,temp2]
	XO_x1,XO_x2 = 0,0
	XO_ans = 0
	XO_q_ans = 0
	XO_question = ''
	XO_Ximg = pygame.image.load('assets\\buttons\\X_button_.png').convert()
	XO_Oimg = pygame.image.load('assets\\buttons\\O_button.png').convert()
	XO_win = False
	XO_lose = False
	XO_rect = [temp1.get_rect(topleft=(116,103)),temp1.get_rect(topleft=(243,103)),temp1.get_rect(topleft=(370,103)),temp1.get_rect(topleft=(116,229)),temp1.get_rect(topleft=(243,229)),temp1.get_rect(topleft=(370,229)),temp1.get_rect(topleft=(116,355)),temp1.get_rect(topleft=(243,355)),temp1.get_rect(topleft=(370,355))]
	XO_index = [0,0,0,0,0,0,0,0,0]
	XO_RAP = None
	XO_AnsButton = []
	temp1 = pygame.image.load('assets\\buttons\\ans_1.png').convert_alpha()
	temp2 = pygame.image.load('assets\\buttons\\ans_2.png').convert_alpha()
	for i in range(4):
		if i == 0:
			temp = T_Button(temp1,temp2,(41,621),i,XO_font)
		elif i == 1:
			temp = T_Button(temp1,temp2,(241,621),i,XO_font)
		elif i == 2:
			temp = T_Button(temp1,temp2,(441,621),i,XO_font)
		elif i == 3:
			temp = T_Button(temp1,temp2,(641,621),i,XO_font)
		XO_AnsButton.append(temp)

	XO_a = [None,None,None]
	XO_a_pos = [None,None,None]
	XO_OK = False
	XO_player_choose_img = pygame.image.load('assets\\buttons\\XO_player_choose.png').convert()
	XO_pos = None
	XO_replay = False
	XO_text = ['Đang là lượt của bạn, hãy chọn một ô']
XO_back_button = N_Button(back1,back2,(0,0),back_XO)
# BackGrounds ===================================================================== #
lop6_bg = pygame.image.load('assets\\backgrounds\\lop6_bg.png').convert()
lop7_bg = pygame.image.load('assets\\backgrounds\\lop7_bg.png').convert()
lop8_bg = pygame.image.load('assets\\backgrounds\\lop8_bg.png').convert()
lop9_bg = pygame.image.load('assets\\backgrounds\\lop9_bg.png').convert()
start_bg = pygame.image.load('assets\\backgrounds\\start_bg.jpg').convert()
choose_class_bg = pygame.image.load('assets\\backgrounds\\choose_class_bg.jpg').convert()
CM_bg = pygame.image.load('assets\\backgrounds\\CM_bg.png').convert()
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
font2 = pygame.font.Font('assets\\arial.TTF',15)
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
			show_label(screen,'Học chương trình lớp 6',font,(0,0,0),(1280/2,660))
		if lop7_button.get_collide():
			show_label(screen,'Học chương trình lớp 7',font,(0,0,0),(1280/2,660))
		if lop8_button.get_collide():
			show_label(screen,'Học chương trình lớp 8',font,(0,0,0),(1280/2,660))
		if lop9_button.get_collide():
			show_label(screen,'Học chương trình lớp 9',font,(0,0,0),(1280/2,660))
	elif lop6:
		if lop6_Dai_I:
			screen.blit(choose_class_bg,(-10,-10))
			back_button_to_l6.run(screen,click,s_m_o_f)
			for i in range(18):
				lop6_buttons_Dai_I[i].run(screen,click,s_m_o_f)
				if lop6_buttons_Dai_I[i].get_collide():
					if i == 0:
						show_label(screen,'Bài 1: TẬP HỢP, PHẦN TỬ CỦA TẬP HỢP',font,(0,0,0),(640,630))
					elif i == 1:
						show_label(screen,'Bài 2: TẬP HỢP CÁC SỐ TỰ NHIÊN',font,(0,0,0),(640,630))
					elif i == 2:
						show_label(screen,'Bài 3: GHI SỐ TỰ NHIÊN',font,(0,0,0),(640,630))
					elif i == 3:
						show_label(screen,'Bài 4: SỐ PHẦN TỬ CỦA TẬP HỢP. TẬP HỢP CON',font,(0,0,0),(640,630))
					elif i == 4:
						show_label(screen,'Bài 5: PHÉP CỘNG VÀ PHÉP NHÂN',font,(0,0,0),(640,630))
					elif i == 5:
						show_label(screen,'Bài 6: PHÉP TRỪ VÀ PHÉP CHIA',font,(0,0,0),(640,630))
					elif i == 6:
						show_label(screen,'Bài 7: LŨY THỪA VỚI SỐ MŨ TỰ NHIÊN. NHÂN HAI LŨY THỪA CÙNG CƠ SỐ',font,(0,0,0),(640,630))
					elif i == 7:
						show_label(screen,'Bài 8: CHIA LŨY THỪA CÙNG CƠ SỐ',font,(0,0,0),(640,630))
					elif i == 8:
						show_label(screen,'Bài 9: THỨ TỰ THỰC HIỆN CÁC PHÉP TÍNH',font,(0,0,0),(640,630))
					elif i == 9:
						show_label(screen,'Bài 10: TÍNH CHẤT CHIA HẾT CỦA MỘT TỔNG',font,(0,0,0),(640,630))
					elif i == 10:
						show_label(screen,f'Bài {i+1}: DẤU HIỆU CHIA HẾT CHO 2, CHO 5',font,(0,0,0),(640,630))
					elif i == 11:
						show_label(screen,f'Bài {i+1}: DẤU HIỆU CHIA HẾT CHO 3, CHO 9',font,(0,0,0),(640,630))
					elif i == 12:
						show_label(screen,f'Bài {i+1}: ƯỚC VÀ BỘI',font,(0,0,0),(640,630))
					elif i == 13:
						show_label(screen,f'Bài {i+1}: SỐ NGUYÊN TỐ. HỢP SỐ. BẢNG SỐ NGUYÊN TỐ',font,(0,0,0),(640,630))
					elif i == 14:
						show_label(screen,f'Bài {i+1}: PHÂN TÍCH RA THỪA SỐ NGUYÊN TỐ',font,(0,0,0),(640,630))
					elif i == 15:
						show_label(screen,f'Bài {i+1}: ƯỚC CHUNG VÀ BỘI CHUNG',font,(0,0,0),(640,630))
					elif i == 16:
						show_label(screen,f'Bài {i+1}: ƯỚC CHUNG LỚN NHẤT',font,(0,0,0),(640,630))
					elif i == 17:
						show_label(screen,f'Bài {i+1}: BỘI CHUNG NHỎ NHẤT',font,(0,0,0),(640,630))

		elif lop6_Dai_II:
			screen.blit(choose_class_bg,(-10,-10))
			back_button_to_l6.run(screen,click,s_m_o_f)
			for i in range(13):
				lop6_buttons_Dai_II[i].run(screen,click,s_m_o_f)
				if lop6_buttons_Dai_II[i].get_collide():
					if i == 0:
						show_label(screen,f'Bài {i+1}: LÀM QUEN VỚI SỐ NGUYÊN ÂM',font,(0,0,0),(640,630))
					elif i == 1:
						show_label(screen,f'Bài {i+1}: TẬP HỢP CÁC SỐ NGUYÊN',font,(0,0,0),(640,630))
					elif i == 2:
						show_label(screen,f'Bài {i+1}: THỨ TỰ TRONG TẬP HỢP CÁC SỐ NGUYÊN',font,(0,0,0),(640,630))
					elif i == 3:
						show_label(screen,f'Bài {i+1}: CỘNG HAI SỐ NGUYÊN CÙNG DẤU',font,(0,0,0),(640,630))
					elif i == 4:
						show_label(screen,f'Bài {i+1}: CỘNG HAI SỐ NGUYÊN KHÁC DẤU',font,(0,0,0),(640,630))
					elif i == 5:
						show_label(screen,f'Bài {i+1}: TÍNH CHẤT CỦA PHÉP CỘNG CÁC SỐ NGUYÊN',font,(0,0,0),(640,630))
					elif i == 6:
						show_label(screen,f'Bài {i+1}: PHÉP TRỪ HAI SỐ NGUYÊN',font,(0,0,0),(640,630))
					elif i == 7:
						show_label(screen,f'Bài {i+1}: QUY TẮC DẤU NGOẶC',font,(0,0,0),(640,630))
					elif i == 8:
						show_label(screen,f'Bài {i+1}: QUY TẮC CHUYỂN VẾ',font,(0,0,0),(640,630))
					elif i == 9:
						show_label(screen,f'Bài {i+1}: NHÂN HAI SỐ NGUYÊN KHÁC DẤU',font,(0,0,0),(640,630))
					elif i == 10:
						show_label(screen,f'Bài {i+1}: NHÂN HAI SÔ NGUYÊN CÙNG DẤU',font,(0,0,0),(640,630))
					elif i == 11:
						show_label(screen,f'Bài {i+1}: TÍNH CHẤT CỦA PHÉP NHÂN',font,(0,0,0),(640,630))
					elif i == 12:
						show_label(screen,f'Bài {i+1}: BỘI VÀ ƯỚC CỦA MỘT SỐ NGUYÊN',font,(0,0,0),(640,630))

		elif lop6_Dai_III:
			screen.blit(choose_class_bg,(-10,-10))
			back_button_to_l6.run(screen,click,s_m_o_f)
			for i in range(17):
				lop6_buttons_Dai_III[i].run(screen,click,s_m_o_f)
				if lop6_buttons_Dai_III[i].get_collide():
					if i == 0:
						show_label(screen,f'Bài {i+1}: MỞ RỘNG KHÁI NIỆM PHÂN SỐ',font,(0,0,0),(640,630))
					elif i == 1:
						show_label(screen,f'Bài {i+1}: PHÂN SỐ BẰNG NHAU',font,(0,0,0),(640,630))
					elif i == 2:
						show_label(screen,f'Bài {i+1}: TÍNH CHẤT CƠ BẢN CỦA PHÂN SỐ',font,(0,0,0),(640,630))
					elif i == 3:
						show_label(screen,f'Bài {i+1}: RÚT GỌN PHÂN SỐ',font,(0,0,0),(640,630))
					elif i == 4:
						show_label(screen,f'Bài {i+1}: QUY ĐỒNG MẪU NHIỀU PHÂN SỐ',font,(0,0,0),(640,630))
					elif i == 5:
						show_label(screen,f'Bài {i+1}: SO SÁNH PHÂN SỐ',font,(0,0,0),(640,630))
					elif i == 6:
						show_label(screen,f'Bài {i+1}: PHÉP CỘNG PHÂN SỐ',font,(0,0,0),(640,630))
					elif i == 7:
						show_label(screen,f'Bài {i+1}: TÍNH CHẤT CƠ BẢN CỦA PHÉP CỘNG PHÂN SỐ',font,(0,0,0),(640,630))
					elif i == 8:
						show_label(screen,f'Bài {i+1}: PHÉP TRỪ PHÂN SỐ',font,(0,0,0),(640,630))
					elif i == 9:
						show_label(screen,f'Bài {i+1}: PHÉP NHÂN PHÂN SỐ',font,(0,0,0),(640,630))
					elif i == 10:
						show_label(screen,f'Bài {i+1}: TÍNH CHẤT CƠ BẢN CỦA PHÉP NHÂN PHÂN SỐ',font,(0,0,0),(640,630))
					elif i == 11:
						show_label(screen,f'Bài {i+1}: PHÉP CHIA PHÂN SỐ',font,(0,0,0),(640,630))
					elif i == 12:
						show_label(screen,f'Bài {i+1}: HỖN SỐ. SỐ THẬP PHÂN. PHẦN TRĂM',font,(0,0,0),(640,630))
					elif i == 13:
						show_label(screen,f'Bài {i+1}: TÌM GIÁ TRỊ PHÂN SỐ CỦA MỘT SỐ CHO TRƯỚC',font,(0,0,0),(640,630))
					elif i == 14:
						show_label(screen,f'Bài {i+1}: TÌM MỘT SỐ BIẾT GIÁ TRỊ CỦA MỘT PHÂN SỐ CỦA NÓ',font,(0,0,0),(640,630))
					elif i == 15:
						show_label(screen,f'Bài {i+1}: TÌM TỈ SỐ CỦA HAI SỐ',font,(0,0,0),(640,630))
					elif i == 16:
						show_label(screen,f'Bài {i+1}: BIỂU ĐỒ PHẦN TRĂM',font,(0,0,0),(640,630))

		elif lop6_Hinh_I:
			screen.blit(choose_class_bg,(-10,-10))
			back_button_to_l6.run(screen,click,s_m_o_f)
			for i in range(10):
				lop6_buttons_Hinh_I[i].run(screen,click,s_m_o_f)
				if lop6_buttons_Hinh_I[i].get_collide():
					if i == 0:
						show_label(screen,f'Bài {i+1}: ĐIỂM. ĐƯỜNG THẰNG',font,(0,0,0),(640,630))
					elif i == 1:
						show_label(screen,f'Bài {i+1}: BA ĐIỂM THẰNG HÀNG',font,(0,0,0),(640,630))
					elif i == 2:
						show_label(screen,f'Bài {i+1}: ĐƯỜNG THẰNG ĐI QUA HAI ĐIỂM',font,(0,0,0),(640,630))
					elif i == 3:
						show_label(screen,f'Bài {i+1}: THỰC HÀNH (KHÔNG CÓ LÝ THUYẾT)',font,(0,0,0),(640,630))
					elif i == 4:
						show_label(screen,f'Bài {i+1}: TIA',font,(0,0,0),(640,630))
					elif i == 5:
						show_label(screen,f'Bài {i+1}: ĐOẠN THẰNG',font,(0,0,0),(640,630))
					elif i == 6:
						show_label(screen,f'Bài {i+1}: ĐỘ DÀI ĐOẠN THẰNG',font,(0,0,0),(640,630))
					elif i == 7:
						show_label(screen,f'Bài {i+1}: KHI NÀO THÌ AM + MB = AB ?',font,(0,0,0),(640,630))
					elif i == 8:
						show_label(screen,f'Bài {i+1}: VẼ ĐOẠN THẲNG CHO BIẾT ĐỘ DÀI',font,(0,0,0),(640,630))
					elif i == 9:
						show_label(screen,f'Bài {i+1}: TRUNG ĐIỂM CỦA ĐOẠN THẲNG',font,(0,0,0),(640,630))
					

		elif lop6_Hinh_II:
			screen.blit(choose_class_bg,(-10,-10))
			back_button_to_l6.run(screen,click,s_m_o_f)
			for i in range(9):
				lop6_buttons_Hinh_II[i].run(screen,click,s_m_o_f)
				if lop6_buttons_Hinh_II[i].get_collide():
					if i == 0:
						show_label(screen,f'Bài {i+1}: NỬA MẶT PHẲNG',font,(0,0,0),(640,630))
					elif i == 1:
						show_label(screen,f'Bài {i+1}: GÓC',font,(0,0,0),(640,630))
					elif i == 2:
						show_label(screen,f'Bài {i+1}: SỐ ĐO GÓC',font,(0,0,0),(640,630))
					elif i == 3:
						show_label(screen,f'Bài {i+1}: KHI NÀO THÌ xOy + yOz = xOz?',font,(0,0,0),(640,630))
					elif i == 4:
						show_label(screen,f'Bài {i+1}: VẼ GÓC CHO BIẾT SỐ ĐO',font,(0,0,0),(640,630))
					elif i == 5:
						show_label(screen,f'Bài {i+1}: TIA PHÂN GIÁC CỦA GÓC',font,(0,0,0),(640,630))
					elif i == 6:
						show_label(screen,f'Bài {i+1}: THỰC HÀNH',font,(0,0,0),(640,630))
					elif i == 7:
						show_label(screen,f'Bài {i+1}: ĐƯỜNG TRÒN',font,(0,0,0),(640,630))
					elif i == 8:
						show_label(screen,f'Bài {i+1}: TAM GIÁC',font,(0,0,0),(640,630))
		elif XO_l6:
			screen.blit(XO_bg,(0,0))
			if XO_wait:
				if XO_O[0] == XO_O[1] == XO_O[2] == 'O' or XO_O[3] == XO_O[4] == XO_O[5] == 'O' or XO_O[6] == XO_O[7] == XO_O[8] == 'O' or XO_O[0] == XO_O[3] == XO_O[6] == 'O' or XO_O[1] == XO_O[4] == XO_O[7] == 'O' or XO_O[2] == XO_O[5] == XO_O[8] == 'O' or XO_O[0] == XO_O[4] == XO_O[8] == 'O' or XO_O[2] == XO_O[4] == XO_O[6] == 'O':
					XO_win = True
					XO_wait = False
					XO_text.append('Chúc mừng, bạn đã chiến thắng!!')
					
				elif XO_O[0] == XO_O[1] == XO_O[2] == 'X' or XO_O[3] == XO_O[4] == XO_O[5] == 'X' or XO_O[6] == XO_O[7] == XO_O[8] == 'X' or XO_O[0] == XO_O[3] == XO_O[6] == 'X' or XO_O[1] == XO_O[4] == XO_O[7] == 'X' or XO_O[2] == XO_O[5] == XO_O[8] == 'X' or XO_O[0] == XO_O[4] == XO_O[8] == 'X' or XO_O[2] == XO_O[4] == XO_O[6] == 'X':
					XO_lose = True
					XO_wait = False
					XO_text.append('Máy tính đã chiến thắng, chúc bạn may mắn lần sau')
				if XO_turn == 'c':
					XO_turn = 'p'
					XO_ingenerate = True
					while XO_ingenerate:
						XO_c_pick = random.randint(0,8)
						if XO_O[XO_c_pick] == 'n':
							XO_O[XO_c_pick] = 'X'
							XO_ingenerate = False
							time.sleep(1)
							XO_text.append(f'<c>Máy tính chọn ô số {XO_c_pick}           ')
							XO_text.append('<o>Lượt của bạn, hãy chọn một ô:         ')

				for i in range(9):
					if XO_O[i] == 'n':
						mouse_pos = pygame.mouse.get_pos()
						if XO_rect[i].collidepoint(mouse_pos):
							XO_index[i] = 1
							if click and pygame.mouse.get_pressed()[0]:
								XO_selected = i
								XO_wait = False
								s_m_o_f()
								XO_text.append(f'<o>Đã chọn ô {i}                ')
						else:
							XO_index[i] = 0

						screen.blit(XO_button[XO_index[i]],XO_rect[i])
					elif XO_O[i] == 'X':
						if i == 0:
							screen.blit(XO_Ximg,(116,103))
						elif i == 1:
							screen.blit(XO_Ximg,(243,103))
						elif i == 2:
							screen.blit(XO_Ximg,(370,103))
						elif i == 3:
							screen.blit(XO_Ximg,(116,229))
						elif i == 4:
							screen.blit(XO_Ximg,(243,229))
						elif i == 5:
							screen.blit(XO_Ximg,(370,229))
						elif i == 6:
							screen.blit(XO_Ximg,(116,355))
						elif i == 7:
							screen.blit(XO_Ximg,(243,355))
						elif i == 8:
							screen.blit(XO_Ximg,(370,355))
					elif XO_O[i] == 'O':
						if i == 0:
							screen.blit(XO_Oimg,(116,103))
						elif i == 1:
							screen.blit(XO_Oimg,(243,103))
						elif i == 2:
							screen.blit(XO_Oimg,(370,103))
						elif i == 3:
							screen.blit(XO_Oimg,(116,229))
						elif i == 4:
							screen.blit(XO_Oimg,(243,229))
						elif i == 5:
							screen.blit(XO_Oimg,(370,229))
						elif i == 6:
							screen.blit(XO_Oimg,(116,355))
						elif i == 7:
							screen.blit(XO_Oimg,(243,355))
						elif i == 8:
							screen.blit(XO_Oimg,(370,355))
			elif XO_wait == False and XO_win == False and XO_lose == False:
				if XO_turn == 'p':
					XO_text.append('<o> Hãy trả lời câu hỏi để tích "O"       ')
					XO_turn = 'c'
					XO_x1 = random.randint(1,10)
					XO_x2 = random.randint(1,100)
					XO_ans = random.randint(1,10)
					XO_q_ans = XO_x1*XO_ans+XO_x2
					XO_question = f'{XO_x1} x (?) + {XO_x2} = {XO_q_ans}'
					XO_qIMG = XO_font.render(XO_question,True,(0,0,0))
					XO_qRECT = XO_qIMG.get_rect(topleft=(47,575))
					XO_RAP = random.randint(0,3)
					XO_AnsButton[XO_RAP].set_text(str(XO_ans))
					for i in range(3):
						while True:
							XO_a[i] = random.randint(1,10)
							for j in range(3):
								if j != i:
									if XO_a[i] == XO_a[j] or XO_a[i] == XO_ans:
										XO_OK = False
										break
									XO_OK = True

							if XO_OK and XO_a[i] != XO_ans:
								break
					j = 0
					for i in range(4):
						if i != XO_RAP:
							XO_AnsButton[i].set_text(XO_a[j])
							j += 1
				for i in range(4):
					XO_AnsButton[i].run(screen,click,s_m_o_f)
					if XO_AnsButton[i].get_return() == XO_RAP:
						XO_O[XO_selected] = 'O'
						XO_selected = None
						XO_wait = True
						XO_text.append('<o> Bạn đã trả lời chính xác, đã đánh dấu!')
					elif XO_AnsButton[i].get_return() != XO_RAP and XO_AnsButton[i].get_return() != None:
						XO_selected = None
						XO_wait = True
						XO_text.append('<!> Thôi, sai mất rồi :(                  ')

				screen.blit(XO_qIMG,XO_qRECT)
				if XO_selected == 0:
					XO_pos = (116,103)
				elif XO_selected == 1:
					XO_pos =(243,103)
				elif XO_selected == 2:
					XO_pos =(370,103)
				elif XO_selected == 3:
					XO_pos =(116,229)
				elif XO_selected == 4:
					XO_pos =(243,229)
				elif XO_selected == 5:
					XO_pos =(370,229)
				elif XO_selected == 6:
					XO_pos =(116,355)
				elif XO_selected == 7:
					XO_pos =(243,355)
				elif XO_selected == 8:
					XO_pos =(370,355)
				screen.blit(XO_player_choose_img,XO_pos)
				for i in range(9):
					if XO_O[i] == 'X':
						if i == 0:
							screen.blit(XO_Ximg,(116,103))
						elif i == 1:
							screen.blit(XO_Ximg,(243,103))
						elif i == 2:
							screen.blit(XO_Ximg,(370,103))
						elif i == 3:
							screen.blit(XO_Ximg,(116,229))
						elif i == 4:
							screen.blit(XO_Ximg,(243,229))
						elif i == 5:
							screen.blit(XO_Ximg,(370,229))
						elif i == 6:
							screen.blit(XO_Ximg,(116,355))
						elif i == 7:
							screen.blit(XO_Ximg,(243,355))
						elif i == 8:
							screen.blit(XO_Ximg,(370,355))
					elif XO_O[i] == 'O':
						if i == 0:
							screen.blit(XO_Oimg,(116,103))
						elif i == 1:
							screen.blit(XO_Oimg,(243,103))
						elif i == 2:
							screen.blit(XO_Oimg,(370,103))
						elif i == 3:
							screen.blit(XO_Oimg,(116,229))
						elif i == 4:
							screen.blit(XO_Oimg,(243,229))
						elif i == 5:
							screen.blit(XO_Oimg,(370,229))
						elif i == 6:
							screen.blit(XO_Oimg,(116,355))
						elif i == 7:
							screen.blit(XO_Oimg,(243,355))
						elif i == 8:
							screen.blit(XO_Oimg,(370,355))



			elif XO_lose == True:
				XO_replay_button.run(screen,click,s_m_o_f)
				for i in range(9):
					if XO_O[i] == 'n':
						mouse_pos = pygame.mouse.get_pos()
						if XO_rect[i].collidepoint(mouse_pos):
							XO_index[i] = 1
							if click and pygame.mouse.get_pressed()[0]:
								XO_selected = i
								XO_wait = False
								s_m_o_f()
								XO_text.append(f'<o>Đã chọn ô {i}                ')
						else:
							XO_index[i] = 0

						screen.blit(XO_button[XO_index[i]],XO_rect[i])
					elif XO_O[i] == 'X':
						if i == 0:
							screen.blit(XO_Ximg,(116,103))
						elif i == 1:
							screen.blit(XO_Ximg,(243,103))
						elif i == 2:
							screen.blit(XO_Ximg,(370,103))
						elif i == 3:
							screen.blit(XO_Ximg,(116,229))
						elif i == 4:
							screen.blit(XO_Ximg,(243,229))
						elif i == 5:
							screen.blit(XO_Ximg,(370,229))
						elif i == 6:
							screen.blit(XO_Ximg,(116,355))
						elif i == 7:
							screen.blit(XO_Ximg,(243,355))
						elif i == 8:
							screen.blit(XO_Ximg,(370,355))
					elif XO_O[i] == 'O':
						if i == 0:
							screen.blit(XO_Oimg,(116,103))
						elif i == 1:
							screen.blit(XO_Oimg,(243,103))
						elif i == 2:
							screen.blit(XO_Oimg,(370,103))
						elif i == 3:
							screen.blit(XO_Oimg,(116,229))
						elif i == 4:
							screen.blit(XO_Oimg,(243,229))
						elif i == 5:
							screen.blit(XO_Oimg,(370,229))
						elif i == 6:
							screen.blit(XO_Oimg,(116,355))
						elif i == 7:
							screen.blit(XO_Oimg,(243,355))
						elif i == 8:
							screen.blit(XO_Oimg,(370,355))
				if XO_replay:
					XO_font = pygame.font.Font(None,25)
					XO_selected = None
					XO_running = True
					XO_wait = True
					XO_O = ['n','n','n','n','n','n','n','n','n']
					XO_turn = 'p'
					XO_bg = pygame.image.load('assets\\backgrounds\\X_O_bg.png').convert()
					temp1 = pygame.image.load('assets\\buttons\\X_O_button.png').convert()
					temp2 = pygame.image.load('assets\\buttons\\X_O_button_1.png').convert()
					XO_button = [temp1,temp2]
					XO_x1,XO_x2 = 0,0
					XO_ans = 0
					XO_q_ans = 0
					XO_question = ''
					XO_Ximg = pygame.image.load('assets\\buttons\\X_button_.png').convert()
					XO_Oimg = pygame.image.load('assets\\buttons\\O_button.png').convert()
					XO_win = False
					XO_lose = False
					XO_rect = [temp1.get_rect(topleft=(116,103)),temp1.get_rect(topleft=(243,103)),temp1.get_rect(topleft=(370,103)),temp1.get_rect(topleft=(116,229)),temp1.get_rect(topleft=(243,229)),temp1.get_rect(topleft=(370,229)),temp1.get_rect(topleft=(116,355)),temp1.get_rect(topleft=(243,355)),temp1.get_rect(topleft=(370,355))]
					XO_index = [0,0,0,0,0,0,0,0,0]
					XO_RAP = None
					XO_AnsButton = []
					temp1 = pygame.image.load('assets\\buttons\\ans_1.png').convert_alpha()
					temp2 = pygame.image.load('assets\\buttons\\ans_2.png').convert_alpha()
					for i in range(4):
						if i == 0:
							temp = T_Button(temp1,temp2,(41,621),i,XO_font)
						elif i == 1:
							temp = T_Button(temp1,temp2,(241,621),i,XO_font)
						elif i == 2:
							temp = T_Button(temp1,temp2,(441,621),i,XO_font)
						elif i == 3:
							temp = T_Button(temp1,temp2,(641,621),i,XO_font)
						XO_AnsButton.append(temp)

					XO_a = [None,None,None]
					XO_a_pos = [None,None,None]
					XO_OK = False
					XO_player_choose_img = pygame.image.load('assets\\buttons\\XO_player_choose.png').convert()
					XO_pos = None
					XO_replay = False
					XO_text = ['Đang là lượt của bạn, hãy chọn một ô']
			elif XO_win == True:
				XO_replay_button.run(screen,click,s_m_o_f)
				for i in range(9):
					if XO_O[i] == 'n':
						mouse_pos = pygame.mouse.get_pos()
						if XO_rect[i].collidepoint(mouse_pos):
							XO_index[i] = 1
							if click and pygame.mouse.get_pressed()[0]:
								XO_selected = i
								XO_wait = False
								s_m_o_f()
								XO_text.append(f'<o>Đã chọn ô {i}                ')
						else:
							XO_index[i] = 0

						screen.blit(XO_button[XO_index[i]],XO_rect[i])
					elif XO_O[i] == 'X':
						if i == 0:
							screen.blit(XO_Ximg,(116,103))
						elif i == 1:
							screen.blit(XO_Ximg,(243,103))
						elif i == 2:
							screen.blit(XO_Ximg,(370,103))
						elif i == 3:
							screen.blit(XO_Ximg,(116,229))
						elif i == 4:
							screen.blit(XO_Ximg,(243,229))
						elif i == 5:
							screen.blit(XO_Ximg,(370,229))
						elif i == 6:
							screen.blit(XO_Ximg,(116,355))
						elif i == 7:
							screen.blit(XO_Ximg,(243,355))
						elif i == 8:
							screen.blit(XO_Ximg,(370,355))
					elif XO_O[i] == 'O':
						if i == 0:
							screen.blit(XO_Oimg,(116,103))
						elif i == 1:
							screen.blit(XO_Oimg,(243,103))
						elif i == 2:
							screen.blit(XO_Oimg,(370,103))
						elif i == 3:
							screen.blit(XO_Oimg,(116,229))
						elif i == 4:
							screen.blit(XO_Oimg,(243,229))
						elif i == 5:
							screen.blit(XO_Oimg,(370,229))
						elif i == 6:
							screen.blit(XO_Oimg,(116,355))
						elif i == 7:
							screen.blit(XO_Oimg,(243,355))
						elif i == 8:
							screen.blit(XO_Oimg,(370,355))
				if XO_replay:
					XO_font = pygame.font.Font(None,25)
					XO_selected = None
					XO_running = True
					XO_wait = True
					XO_O = ['n','n','n','n','n','n','n','n','n']
					XO_turn = 'p'
					XO_bg = pygame.image.load('assets\\backgrounds\\X_O_bg.png').convert()
					temp1 = pygame.image.load('assets\\buttons\\X_O_button.png').convert()
					temp2 = pygame.image.load('assets\\buttons\\X_O_button_1.png').convert()
					XO_button = [temp1,temp2]
					XO_x1,XO_x2 = 0,0
					XO_ans = 0
					XO_q_ans = 0
					XO_question = ''
					XO_Ximg = pygame.image.load('assets\\buttons\\X_button_.png').convert()
					XO_Oimg = pygame.image.load('assets\\buttons\\O_button.png').convert()
					XO_win = False
					XO_lose = False
					XO_rect = [temp1.get_rect(topleft=(116,103)),temp1.get_rect(topleft=(243,103)),temp1.get_rect(topleft=(370,103)),temp1.get_rect(topleft=(116,229)),temp1.get_rect(topleft=(243,229)),temp1.get_rect(topleft=(370,229)),temp1.get_rect(topleft=(116,355)),temp1.get_rect(topleft=(243,355)),temp1.get_rect(topleft=(370,355))]
					XO_index = [0,0,0,0,0,0,0,0,0]
					XO_RAP = None
					XO_AnsButton = []
					temp1 = pygame.image.load('assets\\buttons\\ans_1.png').convert_alpha()
					temp2 = pygame.image.load('assets\\buttons\\ans_2.png').convert_alpha()
					for i in range(4):
						if i == 0:
							temp = T_Button(temp1,temp2,(41,621),i,XO_font)
						elif i == 1:
							temp = T_Button(temp1,temp2,(241,621),i,XO_font)
						elif i == 2:
							temp = T_Button(temp1,temp2,(441,621),i,XO_font)
						elif i == 3:
							temp = T_Button(temp1,temp2,(641,621),i,XO_font)
						XO_AnsButton.append(temp)

					XO_a = [None,None,None]
					XO_a_pos = [None,None,None]
					XO_OK = False
					XO_player_choose_img = pygame.image.load('assets\\buttons\\XO_player_choose.png').convert()
					XO_pos = None
					XO_replay = False
					XO_text = ['Đang là lượt của bạn, hãy chọn một ô']
			
			if len(XO_text) > 15:
				list_temp = []
				for i in range(len(XO_text)-15,16):
					temp = XO_text[i]
					list_temp.append(temp)
				XO_text = list_temp
			show_label_tl(screen,XO_text,font,(740,147))
			XO_back_button.run(screen,click,s_m_o_f)

		else:
			screen.blit(lop6_bg,(0,0))
			back_button_to_sc6.run(screen,click,s_m_o_f)
			Chuong_I_Dai_Button.run(screen,click,s_m_o_f)
			Chuong_I_Hinh_Button.run(screen,click,s_m_o_f)

			Chuong_II_Dai_Button.run(screen,click,s_m_o_f)
			Chuong_II_Hinh_Button.run(screen,click,s_m_o_f)

			Chuong_III_Dai_Button.run(screen,click,s_m_o_f)

			X_O_game6.run(screen,click,s_m_o_f)
			if Chuong_I_Dai_Button.get_collide():
				show_label(screen,'CHƯƠNG I: ÔN TẬP VÀ BỔ TÚC KIẾN THỨC VỀ SỐ TỰ NHIÊN',font,(0,0,0),(640,630))
			if Chuong_I_Hinh_Button.get_collide():
				show_label(screen,'CHƯƠNG I: ĐOẠN THẲNG',font,(0,0,0),(640,630))
			if Chuong_II_Dai_Button.get_collide():
				show_label(screen,'CHƯƠNG II: SỐ NGUYÊN',font,(0,0,0),(640,630))
			if Chuong_II_Hinh_Button.get_collide():
				show_label(screen,'CHƯƠNG II: PHÂN SỐ',font,(0,0,0),(640,630))
			if Chuong_III_Dai_Button.get_collide():
				show_label(screen,'CHƯƠNG III: GÓC',font,(0,0,0),(640,630))
	elif lop7:
		if lop7_Dai_I:
			screen.blit(choose_class_bg,(-10,-10))
			back_button_to_l7.run(screen,click,s_m_o_f)
			for i in range(12):
				lop7_buttons_Dai_I[i].run(screen,click,s_m_o_f)
				if lop7_buttons_Dai_I[i].get_collide():
					if i == 0:
						show_label(screen, f'BÀI {i+1}: TẬP HỢP Q CÁC SỐ HỮU TỈ', font, (0,0,0), (640,630))
					elif i == 1:
						show_label(screen, f'BÀI {i+1}: CỘNG TRỪ SỐ HỮU TỈ', font, (0,0,0), (640,630))
					elif i == 2:
						show_label(screen, f'BÀI {i+1}: NHÂN, CHIA CÁC SỐ HỮU TỈ', font, (0,0,0), (640,630))
					elif i == 3:
						show_label(screen, f'BÀI {i+1}: GIÁ TRỊ TUYỆT ĐỐI CỦA MỘT SÔ HỮU TỈ. CỘNG, TRỪ, NHÂN CHIA SỐ THẬP PHÂN', font, (0,0,0), (640,630))
					elif i == 4:
						show_label(screen, f'BÀI {i+1}: LŨY THỪA CỦA MỘT SỐ HỮU TỈ', font, (0,0,0), (640,630))
					elif i == 5:
						show_label(screen, f'BÀI {i+1}: LŨY THỪA CỦA MỘT SỐ HỮU TỈ (TIẾP)', font, (0,0,0), (640,630))
					elif i == 6:
						show_label(screen, f'BÀI {i+1}: TỈ LỆ THỨC', font, (0,0,0), (640,630))
					elif i == 7:
						show_label(screen, f'BÀI {i+1}: TÍNH CHẤT CỦA DÃY TỈ SỐ BẰNG NHAU', font, (0,0,0), (640,630))
					elif i == 8:
						show_label(screen, f'BÀI {i+1}: SỐ THẬP PHÂN HỮU HẠN. SỐ THẬP PHÂN VÔ HẠN TUẦN HOÀN', font, (0,0,0), (640,630))
					elif i == 9:
						show_label(screen, f'BÀI {i+1}: LÀM TRÒN SỐ', font, (0,0,0), (640,630))
					elif i == 10:
						show_label(screen, f'BÀI {i+1}: SỐ VÔ TỈ. KHÁI NIỆM VỀ CĂN BẬC HAI', font, (0,0,0), (640,630))
					elif i == 11:
						show_label(screen, f'BÀI {i+1}: SỐ THỰC', font, (0,0,0), (640,630))
		elif lop7_Dai_II:
			screen.blit(choose_class_bg,(-10,-10))
			back_button_to_l7.run(screen,click,s_m_o_f)
			for i in range(7):
				lop7_buttons_Dai_II[i].run(screen,click,s_m_o_f)
				if lop7_buttons_Dai_II[i].get_collide():
					if i == 0:
						show_label(screen, f'BÀI {i+1}: ĐẠI LƯỢNG TỈ LỆ THUẬN', font, (0,0,0), (640,630))
					elif i == 1:
						show_label(screen, f'BÀI {i+1}: MỘT SỐ BÀI TOÁN VỀ ĐẠI LƯỢNG TỈ LỆ THUẬN', font, (0,0,0), (640,630))
					elif i == 2:
						show_label(screen, f'BÀI {i+1}: ĐẠI LƯỢNG TỈ LỆ NGHỊCH', font, (0,0,0), (640,630))
					elif i == 3:
						show_label(screen, f'BÀI {i+1}: MỘT SỐ BÀI TOÁN VỀ ĐẠI LƯỢNG TỈ LỆ NGHỊCH', font, (0,0,0), (640,630))
					elif i == 4:
						show_label(screen, f'BÀI {i+1}: HÀM SỐ', font, (0,0,0), (640,630))
					elif i == 5:
						show_label(screen, f'BÀI {i+1}: MẶT PHẲNG TỌA ĐỘ', font, (0,0,0), (640,630))
					elif i == 6:
						show_label(screen, f'BÀI {i+1}: ĐỒ THỊ HÀM SỐ y = ax (a khác 0)', font, (0,0,0), (640,630))
		elif lop7_Dai_III:
			screen.blit(choose_class_bg,(-10,-10))
			back_button_to_l7.run(screen,click,s_m_o_f)
			for i in range(4):
				lop7_buttons_Dai_III[i].run(screen,click,s_m_o_f)
				if lop7_buttons_Dai_III[i].get_collide():
					if i == 0:
						show_label(screen, f'BÀI {i+1}: THU THẬP SỐ LIỆU THỐNG KÊ, TẦN SỐ', font, (0,0,0), (640,630))
					elif i == 1:
						show_label(screen, f'BÀI {i+1}: BẢNG "TẦN SỐ" CÁC GIÁ TRỊ CỦA DẤU HIỆU*', font, (0,0,0), (640,630))
					elif i == 2:
						show_label(screen, f'BÀI {i+1}: BIỂU ĐỒ', font, (0,0,0), (640,630))
					elif i == 3:
						show_label(screen, f'BÀI {i+1}: SỐ TRUNG BÌNH CỘNG', font, (0,0,0), (640,630))
		elif lop7_Dai_IV:
			screen.blit(choose_class_bg,(-10,-10))
			back_button_to_l7.run(screen,click,s_m_o_f)
			for i in range(9):
				lop7_buttons_Dai_IV[i].run(screen,click,s_m_o_f)
				if lop7_buttons_Dai_IV[i].get_collide():
					if i == 0:
						show_label(screen, f'BÀI {i+1}: KHÁI NIỆM VỀ BIỂU THỨC ĐẠI SỐ', font, (0,0,0), (640,630))
					elif i == 1:
						show_label(screen, f'BÀI {i+1}: GIÁ TRỊ CỦA MỘT BIỂU THỨC ĐẠI SỐ', font, (0,0,0), (640,630))
					elif i == 2:
						show_label(screen, f'BÀI {i+1}: ĐƠN THỨC', font, (0,0,0), (640,630))
					elif i == 3:
						show_label(screen, f'BÀI {i+1}: ĐƠN THỨC ĐỒNG DẠNG', font, (0,0,0), (640,630))
					elif i == 4:
						show_label(screen, f'BÀI {i+1}: ĐA THỨC', font, (0,0,0), (640,630))
					elif i == 5:
						show_label(screen, f'BÀI {i+1}: CỘNG, TRỪ ĐA THỨC', font, (0,0,0), (640,630))
					elif i == 6:
						show_label(screen, f'BÀI {i+1}: ĐA THỨC MỘT BIẾN', font, (0,0,0), (640,630))
					elif i == 7:
						show_label(screen, f'BÀI {i+1}: CỘNG TRỪ ĐA THỨC MỘT BIẾN', font, (0,0,0), (640,630))
					elif i == 8:
						show_label(screen, f'BÀI {i+1}: NGHIỆM CỦA ĐA THỨC MỘT BIẾN', font, (0,0,0), (640,630))
		elif lop7_Hinh_I:
			screen.blit(choose_class_bg,(-10,-10))
			back_button_to_l7.run(screen,click,s_m_o_f)
			for i in range(7):
				lop7_buttons_Hinh_I[i].run(screen,click,s_m_o_f)
				if lop7_buttons_Hinh_I[i].get_collide():
					if i == 0:
						show_label(screen, f'BÀI {i+1}: HAI GÓC ĐỐI ĐỈNH', font, (0,0,0), (640,630))
					elif i == 1:
						show_label(screen, f'BÀI {i+1}: HAI ĐƯỜNG THẲNG VUÔNG GÓC', font, (0,0,0), (640,630))
					elif i == 2:
						show_label(screen, f'BÀI {i+1}: CÁC GÓC TẠO BỞI MỘT ĐƯỜNG THẲNG CẮT HAI ĐƯỜNG THẲNG', font, (0,0,0), (640,630))
					elif i == 3:
						show_label(screen, f'BÀI {i+1}: HAI ĐƯỜNG THẲNG SONG SONG', font, (0,0,0), (640,630))
					elif i == 4:
						show_label(screen, f'BÀI {i+1}: TIÊN ĐỀ Ơ-CLIT VỀ ĐƯỜNG THẲNG SONG SONG', font, (0,0,0), (640,630))
					elif i == 5:
						show_label(screen, f'BÀI {i+1}: TỪ VUÔNG GÓC ĐẾN SONG SONG', font, (0,0,0), (640,630))
					elif i == 6:
						show_label(screen, f'BÀI {i+1}: ĐỊNH LÍ', font, (0,0,0), (640,630))
		elif lop7_Hinh_II:
			screen.blit(choose_class_bg,(-10,-10))
			back_button_to_l7.run(screen,click,s_m_o_f)
			for i in range(9):
				lop7_buttons_Hinh_II[i].run(screen,click,s_m_o_f)
				if lop7_buttons_Hinh_II[i].get_collide():
					if i == 0:
						show_label(screen, f'BÀI {i+1}: TỔNG BA GÓC CỦA TAM GIÁC', font, (0,0,0), (640,630))
					elif i == 1:
						show_label(screen, f'BÀI {i+1}: HAI TAM GIÁC BẰNG NHAU', font, (0,0,0), (640,630))
					elif i == 2:
						show_label(screen, f'BÀI {i+1}: TRƯỜNG HỢP BẰNG NHAU THỨ NHẤT CỦA TAM GIÁC. CẠNH - CẠNH - CẠNH (c.c.c)', font, (0,0,0), (640,630))
					elif i == 3:
						show_label(screen, f'BÀI {i+1}: TRƯỜNG HỢP BẰNG NHAU THỨ HAI CỦA TAM GIÁC. CẠNH - GÓC - CẠNH (c.g.c)', font, (0,0,0), (640,630))
					elif i == 4:
						show_label(screen, f'BÀI {i+1}: TRƯỜNG HỢP BẰNG NHAU THỨ BA CỦA TAM GIÁC. GÓC - CẠNH - GÓC (g.c.g)', font, (0,0,0), (640,630))
					elif i == 5:
						show_label(screen, f'BÀI {i+1}: TAM GIÁC CÂN', font, (0,0,0), (640,630))
					elif i == 6:
						show_label(screen, f'BÀI {i+1}: ĐỊNH LÍ Pi-ta-go', font, (0,0,0), (640,630))
					elif i == 7:
						show_label(screen, f'BÀI {i+1}: CÁC TRƯỜNG HỢP BẰNG NHAU CỦA TAM GIÁC VUÔNG', font, (0,0,0), (640,630))
					elif i == 8:
						show_label(screen, f'BÀI {i+1}: THỰC HÀNH NGOÀI TRỜI', font, (0,0,0), (640,630))
		elif lop7_Hinh_III:
			screen.blit(choose_class_bg,(-10,-10))
			back_button_to_l7.run(screen,click,s_m_o_f)
			for i in range(9):
				lop7_buttons_Hinh_III[i].run(screen,click,s_m_o_f)
				if lop7_buttons_Hinh_III[i].get_collide():
					if i == 0:
						show_label(screen, f'BÀI {i+1}: QUAN HỆ GIỮA GÓC VÀ CẠNH ĐỐI DIỆN TRONG MỘT TAM GIÁC', font, (0,0,0), (640,630))
					elif i == 1:
						show_label(screen, f'BÀI {i+1}: QUAN HỆ GIỮA ĐƯỜNG VUÔNG GÓC VÀ ĐƯỜNG XIÊN, ĐƯỜNG XIÊN VÀ HÌNH CHIẾU', font, (0,0,0), (640,630))
					elif i == 2:
						show_label(screen, f'BÀI {i+1}: QUAN HỆ GIỮA CÁC CẠNH CỦA MỘT TAM GIÁC. BẤT ĐẲNG THỨC TAM GIÁC', font, (0,0,0), (640,630))
					elif i == 3:
						show_label(screen, f'BÀI {i+1}: TÍNH CHẤT BA ĐƯỜNG TRUNG TUYẾN CỦA TAM GIÁC', font, (0,0,0), (640,630))
					elif i == 4:
						show_label(screen, f'BÀI {i+1}: TÍNH CHẤT TIA PHÂN GIÁC CỦA MỘT GÓC', font, (0,0,0), (640,630))
					elif i == 5:
						show_label(screen, f'BÀI {i+1}: TÍNH CHẤT BA ĐƯỜNG PHÂN GIÁC CỦA TAM GIÁC', font, (0,0,0), (640,630))
					elif i == 6:
						show_label(screen, f'BÀI {i+1}: TÍNH CHẤT ĐƯỜNG TRUNG TRỰC CỦA MỘT ĐOẠN THẲNG', font, (0,0,0), (640,630))
					elif i == 7:
						show_label(screen, f'BÀI {i+1}: TÍNH CHẤT BA ĐƯỜNG TRUNG TRỰC CỦA TAM GIÁC', font, (0,0,0), (640,630))
					elif i == 8:
						show_label(screen, f'BÀI {i+1}: TÍNH CHẤT BA ĐƯỜNG CAO CỦA TAM GIÁC', font, (0,0,0), (640,630))
		elif CM_l7:
			if CM_ingenerate:
				for i in range(6):
					CM_var[i] = random.randrange(-20,20)
					if CM_var[i] >= 0 and i != 0:
						CM_tvar[i] = '+'+ str(CM_var[i])
					elif CM_var[i] >= 0 and i == 0:
						CM_tvar[i] = str(CM_var[i])
					elif CM_var[i] < 0:
						CM_tvar[i] = str(CM_var[i])
				CM_WTFind = random.choice(['x','xy','y'])
				if CM_WTFind == 'x':
					CM_ans = CM_var[0] + CM_var[3]
				elif CM_WTFind == 'xy':
					CM_ans = CM_var[1]
				elif CM_WTFind == 'y':
					CM_ans = CM_var[2] + CM_var[4]

				CM_question = f'Cho đa thức {CM_tvar[0]}x{CM_tvar[1]}xy{CM_tvar[2]}y{CM_tvar[3]}x{CM_tvar[4]}y{CM_tvar[5]} . Hãy tìm hệ số của {CM_WTFind}.'
				CM_ingenerate = False
			screen.blit(CM_bg,(0,0))
			show_label_topleft(screen,CM_question,font,(0,0,0),(78,55))
			show_label_topleft(screen,str(CM_t),font,(0,0,0),(78,70))
			for i in range(10):
				CM_buttons[i].run(screen,click,s_m_o_f)
		else:
			screen.blit(lop7_bg,(0,0))
			back_button_to_sc7.run(screen,click,s_m_o_f)
			Chuong_I_Dai_Button.run(screen,click,s_m_o_f)
			Chuong_I_Hinh_Button.run(screen,click,s_m_o_f)

			Chuong_II_Dai_Button.run(screen,click,s_m_o_f)
			Chuong_II_Hinh_Button.run(screen,click,s_m_o_f)

			Chuong_III_Dai_Button.run(screen,click,s_m_o_f)
			Chuong_III_Hinh_Button.run(screen,click,s_m_o_f)

			Chuong_IV_Dai_Button.run(screen,click,s_m_o_f)
			if Chuong_I_Dai_Button.get_collide():
				show_label(screen,'CHƯƠNG I: SỐ HỮU TỈ. SỐ THỰC',font,(0,0,0),(1280/2,660))
			elif Chuong_II_Dai_Button.get_collide():
				show_label(screen,'CHƯƠNG II: HÀM SỐ VÀ ĐỒ THỊ',font,(0,0,0),(1280/2,660))
			elif Chuong_III_Dai_Button.get_collide():
				show_label(screen,'CHƯƠNG III: THỐNG KÊ',font,(0,0,0),(1280/2,660))
			elif Chuong_IV_Dai_Button.get_collide():
				show_label(screen,'CHƯƠNG IV: BIỂU THỨC ĐẠI SỐ',font,(0,0,0),(1280/2,660))
			elif Chuong_I_Hinh_Button.get_collide():
				show_label(screen,'CHƯƠNG I: ĐƯỜNG THẲNG VUÔNG GÓC',font,(0,0,0),(1280/2,660))
			elif Chuong_II_Hinh_Button.get_collide():
				show_label(screen,'CHƯƠNG II: TAM GIÁC',font,(0,0,0),(1280/2,660))
			elif Chuong_III_Hinh_Button.get_collide():
				show_label(screen,'CHƯƠNG III: QUAN HỆ GIỮA CÁC YẾU TỐ TRONG TAM GIÁC. CÁC ĐƯỜNG ĐỒNG QUY CỦA TAM GIÁC',font,(0,0,0),(1280/2,700))
	elif lop8:
		if lop8_Dai_I:
			screen.blit(choose_class_bg,(-10,-10))
			back_button_to_l8.run(screen,click,s_m_o_f)
			for i in range(9):
				lop8_buttons_Dai_I[i].run(screen,click,s_m_o_f)
				if lop8_buttons_Dai_I[i].get_collide():
					if i == 0:
						show_label(screen, f'BÀI {i+1}: NHÂN ĐƠN THỨC VỚI ĐƠN THỨC', font, (0,0,0), (640,630))
					elif i == 1:
						show_label(screen, f'BÀI {i+1}: NHÂN ĐA THỨC VỚI ĐA THỨC', font, (0,0,0), (640,630))
					elif i == 2:
						show_label(screen, f'BÀI {i+1}: NHỮNG HẰNG ĐẲNG THỨC ĐÁNG NHỚ', font, (0,0,0), (640,630))
					elif i == 3:
						show_label(screen, f'BÀI {i+1}: NHỮNG HẰNG ĐẲNG THỨC ĐÁNG NHỚ (tiếp)', font, (0,0,0), (640,630))
					elif i == 4:
						show_label(screen, f'BÀI {i+1}: NHỮNG HẰNG ĐẲNG THỨC ĐÁNG NHỚ (tiếp)', font, (0,0,0), (640,630))
					elif i == 5:
						show_label(screen, f'BÀI {i+1}: PHÂN TÍCH ĐA THỨC THÀNH NHÂN TỬ BẰNG PHƯƠNG PHÁP ĐẶT NHÂN TỬ CHUNG', font, (0,0,0), (640,630))
					elif i == 6:
						show_label(screen, f'BÀI {i+1}: PHÂN TÍCH ĐA THỨC THÀNH NHÂN TỬ BẰNG PHƯƠNG PHÁP DÙNG HẰNG ĐẲNG THỨC', font, (0,0,0), (640,630))
					elif i == 7:
						show_label(screen, f'BÀI {i+1}: PHÂN TÍCH ĐA THỨC THÀNH NHÂN TỬ BẰNG PHƯƠNG PHÁP NHÓM HẠNG TỬ', font, (0,0,0), (640,630))
					elif i == 8:
						show_label(screen, f'BÀI {i+1}: PHÂN TÍCH ĐA THỨC THÀNH NHÂN TỬ BẰNG CÁCH PHỐI HỢP NHIỀU PHƯƠNG PHÁP', font, (0,0,0), (640,630))
		elif lop8_Dai_II:
			screen.blit(choose_class_bg,(-10,-10))
			back_button_to_l8.run(screen,click,s_m_o_f)
			for i in range(9):
				lop8_buttons_Dai_II[i].run(screen,click,s_m_o_f)
				if lop8_buttons_Dai_II[i].run(screen,click,s_m_o_f):
					if i == 0:
						show_label(screen, f'BÀI {i+1}: PHÂN THỨC ĐẠI SỐ', font, (0,0,0), (640,630))
					elif i == 1:
						show_label(screen, f'BÀI {i+1}: TÍNH CHẤT CƠ BẢN CỦA PHÂN THỨC', font, (0,0,0), (640,630))
					elif i == 2:
						show_label(screen, f'BÀI {i+1}: RÚT GỌN PHÂN THỨC', font, (0,0,0), (640,630))
					elif i == 3:
						show_label(screen, f'BÀI {i+1}: QUY ĐỒNG MẪU THỨC NHIỀU PHÂN THỨC', font, (0,0,0), (640,630))
					elif i == 4:
						show_label(screen, f'BÀI {i+1}: PHÉP CỘNG CÁC PHÂN THỨC ĐẠI SỐ', font, (0,0,0), (640,630))
					elif i == 5:
						show_label(screen, f'BÀI {i+1}: PHÉP TRỪ CÁC PHÂN THỨC ĐẠI SỐ', font, (0,0,0), (640,630))
					elif i == 6:
						show_label(screen, f'BÀI {i+1}: PHÉP NHÂN CÁC PHÂN THỨC ĐẠI SỐ', font, (0,0,0), (640,630))
					elif i == 7:
						show_label(screen, f'BÀI {i+1}: PHÉP CHIA CÁC PHÂN THỨC ĐẠI SỐ', font, (0,0,0), (640,630))
					elif i == 8:
						show_label(screen, f'BÀI {i+1}: BIẾN ĐỔI CÁC BIỂU THỨC HỮU TỈ. GIÁ TRỊ CỦA PHÂN THỨC', font, (0,0,0), (640,630))

		elif lop8_Dai_III:
			screen.blit(choose_class_bg,(-10,-10))
			back_button_to_l8.run(screen,click,s_m_o_f)
			for i in range(7):
				lop8_buttons_Dai_III[i].run(screen,click,s_m_o_f)
				if lop8_buttons_Dai_III[i].get_collide():
					if i == 0:
						show_label(screen, f'BÀI {i+1}: MỞ ĐẦU VỀ PHƯƠNG TRÌNH', font, (0,0,0), (640,630))
					elif i == 1:
						show_label(screen, f'BÀI {i+1}: PHƯƠNG TRÌNH BẬC NHẤT MỘT ẨN VÀ CÁCH GIẢI', font, (0,0,0), (640,630))
					elif i == 2:
						show_label(screen, f'BÀI {i+1}: PHƯƠNG TRÌNH ĐƯA ĐƯỢC VỀ DẠNG ax + b = 0', font, (0,0,0), (640,630))
					elif i == 3:
						show_label(screen, f'BÀI {i+1}: PHƯƠNG TRÌNH TÍCH', font, (0,0,0), (640,630))
					elif i == 4:
						show_label(screen, f'BÀI {i+1}: PHƯƠNG TRÌNH CHỨA ẨN Ở MẪU', font, (0,0,0), (640,630))
					elif i == 5:
						show_label(screen, f'BÀI {i+1}: GIẢI BÀI TOÁN BẰNG CÁCH LẬP PHƯƠNG TRÌNH', font, (0,0,0), (640,630))
					elif i == 0:
						show_label(screen, f'BÀI {i+1}: GIẢI BÀI TOÁN BẰNG CÁCH LẬP PHƯƠNG TRÌNH (tiếp)', font, (0,0,0), (640,630))
		elif lop8_Dai_IV:
			screen.blit(choose_class_bg,(-10,-10))
			back_button_to_l8.run(screen,click,s_m_o_f)
			for i in range(5):
				lop8_buttons_Dai_IV[i].run(screen,click,s_m_o_f)
				if lop8_buttons_Dai_IV[i].get_collide():
					if i == 0:
						show_label(screen, f'BÀI {i+1}: LIÊN HỆ GIỮA THỨ TỰ VÀ PHÉP CỘNG', font, (0,0,0), (640,630))
					elif i == 1:
						show_label(screen, f'BÀI {i+1}: LIÊN HỆ GIỮA THỨ TỰ VÀ PHÉP NHÂN', font, (0,0,0), (640,630))
					elif i == 2:
						show_label(screen, f'BÀI {i+1}: BẤT PHƯƠNG TRÌNH MỘT ẨN', font, (0,0,0), (640,630))
					elif i == 3:
						show_label(screen, f'BÀI {i+1}: BẤT PHƯƠNG TRÌNH BẬC NHẤT MỘT ẨN', font, (0,0,0), (640,630))
					elif i == 4:
						show_label(screen, f'BÀI {i+1}: PHƯƠNG TRÌNH CHỨA DẤU GIÁ TRỊ TUYỆT ĐỐI', font, (0,0,0), (640,630))
		elif lop8_Hinh_I:
			screen.blit(choose_class_bg,(-10,-10))
			back_button_to_l8.run(screen,click,s_m_o_f)
			for i in range(12):
				lop8_buttons_Hinh_I[i].run(screen,click,s_m_o_f)
				if lop8_buttons_Hinh_I[i].get_collide():
					if i == 0:
						show_label(screen, f'BÀI {i+1}: TỨ GIÁC', font, (0,0,0), (640,630))
					elif i == 1:
						show_label(screen, f'BÀI {i+1}: HÌNH THANG', font, (0,0,0), (640,630))
					elif i == 2:
						show_label(screen, f'BÀI {i+1}: HÌNH THANG CÂN', font, (0,0,0), (640,630))
					elif i == 3:
						show_label(screen, f'BÀI {i+1}: ĐƯỜNG TRUNG BÌNH CỦA TAM GIÁC, CỦA HÌNH THANG', font, (0,0,0), (640,630))
					elif i == 4:
						show_label(screen, f'BÀI {i+1}: DỰNG HÌNH BẰNG THƯỚC VÀ COMPA. DỰNG HÌNH THANG', font, (0,0,0), (640,630))
					elif i == 5:
						show_label(screen, f'BÀI {i+1}: ĐỐI XỨNG TRỤC', font, (0,0,0), (640,630))
					elif i == 6:
						show_label(screen, f'BÀI {i+1}: HÌNH BÌNH HÀNH', font, (0,0,0), (640,630))
					elif i == 7:
						show_label(screen, f'BÀI {i+1}: ĐỐI XỨNG TÂM', font, (0,0,0), (640,630))
					elif i == 8:
						show_label(screen, f'BÀI {i+1}: HÌNH CHỮ NHẬT', font, (0,0,0), (640,630))
					elif i == 9:
						show_label(screen, f'BÀI {i+1}: ĐƯỜNG THẲNG SAONG SAONG VỚI MỘT ĐƯỜNG THẲNG CHO TRƯỚC', font, (0,0,0), (640,630))
					elif i == 10:
						show_label(screen, f'BÀI {i+1}: HÌNH THOI', font, (0,0,0), (640,630))
					elif i == 11:
						show_label(screen, f'BÀI {i+1}: HÌNH VUÔNG', font, (0,0,0), (640,630))
		elif lop8_Hinh_II:
			screen.blit(choose_class_bg,(-10,-10))
			back_button_to_l8.run(screen,click,s_m_o_f)
			for i in range(6):
				lop8_buttons_Hinh_II[i].run(screen,click,s_m_o_f)
				if lop8_buttons_Hinh_II[i].get_collide():
					if i == 0:
						show_label(screen, f'BÀI {i+1}: ĐA GIÁC. ĐA GIÁC ĐỀU', font, (0,0,0), (640,630))
					elif i == 1:
						show_label(screen, f'BÀI {i+1}: DIỆN TÍCH HÌNH CHỮ NHẬT', font, (0,0,0), (640,630))
					elif i == 2:
						show_label(screen, f'BÀI {i+1}: DIỆN TÍCH HÌNH TAM GIÁC', font, (0,0,0), (640,630))
					elif i == 3:
						show_label(screen, f'BÀI {i+1}: DIỆN TÍCH HÌNH THANG', font, (0,0,0), (640,630))
					elif i == 4:
						show_label(screen, f'BÀI {i+1}: DIỆN TÍCH HÌNH THOI', font, (0,0,0), (640,630))
					elif i == 5:
						show_label(screen, f'BÀI {i+1}: DIỆN TÍCH ĐA GIÁC', font, (0,0,0), (640,630))
		elif lop8_Hinh_III:
			screen.blit(choose_class_bg,(-10,-10))
			back_button_to_l8.run(screen,click,s_m_o_f)
			for i in range(9):
				lop8_buttons_Hinh_III[i].run(screen,click,s_m_o_f)
				if lop8_buttons_Hinh_III[i].get_collide():
					if i == 0:
						show_label(screen, f'BÀI {i+1}: ĐỊNH LÍ TA-LÉT TRONG TAM GIÁC', font, (0,0,0), (640,630))
					elif i == 1:
						show_label(screen, f'BÀI {i+1}: ĐỊNH LÍ ĐẢO VÀ HỆ QUẢ CỦA ĐỊNH LÍ TA-LÉT', font, (0,0,0), (640,630))
					elif i == 2:
						show_label(screen, f'BÀI {i+1}: TÍNH CHẤT ĐƯỜNG PHÂN GIÁC CỦA TAM GIÁC', font, (0,0,0), (640,630))
					elif i == 3:
						show_label(screen, f'BÀI {i+1}: KHÁI NIỆM HAI TAM GIÁC ĐỒNG DẠNG', font, (0,0,0), (640,630))
					elif i == 4:
						show_label(screen, f'BÀI {i+1}: TRƯỜNG HỢP ĐỒNG DẠNG THỨ NHẤT', font, (0,0,0), (640,630))
					elif i == 5:
						show_label(screen, f'BÀI {i+1}: TRƯỜNG HỢP ĐỒNG DẠNG THỨ HAI', font, (0,0,0), (640,630))
					elif i == 6:
						show_label(screen, f'BÀI {i+1}: TRƯỜNG HỢP ĐỒNG DẠNG THỨ BA', font, (0,0,0), (640,630))
					elif i == 7:
						show_label(screen, f'BÀI {i+1}: CÁC TRƯỜNG HỢP ĐỒNG DẠNG CỦA TAM GIÁC VUÔNG', font, (0,0,0), (640,630))
					elif i == 8:
						show_label(screen, f'BÀI {i+1}: ỨNG DỤNG THỰC TẾ CỦA TAM GIÁC ĐỒNG DẠNG', font, (0,0,0), (640,630))
		elif lop8_Hinh_IV:
			screen.blit(choose_class_bg,(-10,-10))
			back_button_to_l8.run(screen,click,s_m_o_f)
			for i in range(9):
				lop8_buttons_Hinh_IV[i].run(screen,click,s_m_o_f)
				if lop8_buttons_Hinh_IV[i].get_collide():
					if i == 0:
						show_label(screen, f'BÀI {i+1}: HÌNH HỘP CHỮ NHẬT', font, (0,0,0), (640,630))
					elif i == 1:
						show_label(screen, f'BÀI {i+1}: HÌNH HỘP CHỮ NHẬT (tiếp)', font, (0,0,0), (640,630))
					elif i == 2:
						show_label(screen, f'BÀI {i+1}: THỂ TÍCH CỦA HÌNH HỘP CHỮ NHẬT', font, (0,0,0), (640,630))
					elif i == 3:
						show_label(screen, f'BÀI {i+1}: HÌNH LĂNG TRỤ ĐỨNG', font, (0,0,0), (640,630))
					elif i == 4:
						show_label(screen, f'BÀI {i+1}: DIỆN TÍCH XUNG QUANH CỦA HÌNH LĂNG TRỤ ĐỨNG', font, (0,0,0), (640,630))
					elif i == 5:
						show_label(screen, f'BÀI {i+1}: THỂ TÍCH CỦA HÌNH LĂNG TRỤ ĐỨNG', font, (0,0,0), (640,630))
					elif i == 6:
						show_label(screen, f'BÀI {i+1}: HÌNH CHÓP ĐỀU VÀ HÌNH CHÓP CỤT ĐỀU', font, (0,0,0), (640,630))
					elif i == 7:
						show_label(screen, f'BÀI {i+1}: DIỆN TÍCH XUNG QUANH CỦA HÌNH CHÓP ĐỀU', font, (0,0,0), (640,630))
					elif i == 8:
						show_label(screen, f'BÀI {i+1}: THỂ TÍCH CỦA HÌNH CHÓP ĐỀU', font, (0,0,0), (640,630))
		else:
			screen.blit(lop8_bg,(0,0))
			back_button_to_sc8.run(screen,click,s_m_o_f)
			Chuong_I_Dai_Button.run(screen,click,s_m_o_f)
			Chuong_I_Hinh_Button.run(screen,click,s_m_o_f)

			Chuong_II_Dai_Button.run(screen,click,s_m_o_f)
			Chuong_II_Hinh_Button.run(screen,click,s_m_o_f)

			Chuong_III_Dai_Button.run(screen,click,s_m_o_f)
			Chuong_III_Hinh_Button.run(screen,click,s_m_o_f)

			Chuong_IV_Dai_Button.run(screen,click,s_m_o_f)
			Chuong_IV_Hinh_Button.run(screen,click,s_m_o_f)
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
			screen.blit(lop9_bg,(0,0))
			back_button_to_sc9.run(screen,click,s_m_o_f)
			Chuong_I_Dai_Button.run(screen,click,s_m_o_f)
			Chuong_I_Hinh_Button.run(screen,click,s_m_o_f)

			Chuong_II_Dai_Button.run(screen,click,s_m_o_f)
			Chuong_II_Hinh_Button.run(screen,click,s_m_o_f)

			Chuong_III_Dai_Button.run(screen,click,s_m_o_f)
			Chuong_III_Hinh_Button.run(screen,click,s_m_o_f)

			Chuong_IV_Dai_Button.run(screen,click,s_m_o_f)
			Chuong_IV_Hinh_Button.run(screen,click,s_m_o_f)
	elif setting:
		screen.fill((255,255,255))
		back_button_to_sc.run(screen,click,s_m_o_f)




	if pygame.mouse.get_pressed()[0] == False and can_c==False:
		can_c = True


	pygame.display.update()
	clock.tick(60)
	check_quit()