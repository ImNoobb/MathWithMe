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


CM_l7 = False
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


lop6_button = A_Button([pygame.image.load('assets\\buttons\\lop6_1.png').convert_alpha(),pygame.image.load('assets\\buttons\\lop6_2.png').convert_alpha(),pygame.image.load('assets\\buttons\\lop6_3.png').convert_alpha(),pygame.image.load('assets\\buttons\\lop6_4.png').convert_alpha(),pygame.image.load('assets\\buttons\\lop6_5.png').convert_alpha(),pygame.image.load('assets\\buttons\\lop6_6.png').convert_alpha()],0.5,(245,180),lop6_cmd)
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


lop7_button = A_Button([pygame.image.load('assets\\buttons\\lop7_1.png').convert_alpha(),pygame.image.load('assets\\buttons\\lop7_2.png').convert_alpha(),pygame.image.load('assets\\buttons\\lop7_3.png').convert_alpha(),pygame.image.load('assets\\buttons\\lop7_4.png').convert_alpha(),pygame.image.load('assets\\buttons\\lop7_5.png').convert_alpha(),pygame.image.load('assets\\buttons\\lop7_6.png').convert_alpha()],0.5,(470,180),lop7_cmd)
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

lop8_button = A_Button([pygame.image.load('assets\\buttons\\lop8_1.png').convert_alpha(),pygame.image.load('assets\\buttons\\lop8_2.png').convert_alpha(),pygame.image.load('assets\\buttons\\lop8_3.png').convert_alpha(),pygame.image.load('assets\\buttons\\lop8_4.png').convert_alpha(),pygame.image.load('assets\\buttons\\lop8_5.png').convert_alpha(),pygame.image.load('assets\\buttons\\lop8_6.png').convert_alpha()],0.5,(695,180),lop8_cmd)
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

lop9_button = A_Button([pygame.image.load('assets\\buttons\\lop9_1.png').convert_alpha(),pygame.image.load('assets\\buttons\\lop9_2.png').convert_alpha(),pygame.image.load('assets\\buttons\\lop9_3.png').convert_alpha(),pygame.image.load('assets\\buttons\\lop9_4.png').convert_alpha(),pygame.image.load('assets\\buttons\\lop9_5.png').convert_alpha(),pygame.image.load('assets\\buttons\\lop9_6.png').convert_alpha()],0.5,(920,180),lop9_cmd)
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
	if y == 0:
		img = pygame.image.load(f'assets\\baigiang\\lop6\\bai{bai+1}.png').convert_alpha()
	else:
		img = pygame.image.load(f'assets\\baigiang\\lop6\\bai{bai+1}_{y}.png').convert_alpha()
	screen.fill((255,255,255))
	if 720-img.get_height()>0:
		scroll_y = 0
	elif scroll_y>0:
		scroll_y = 0
	elif scroll_y<680-img.get_height():
		scroll_y = 680-img.get_height()
	screen.blit(img,(200,scroll_y))
	back_to_class.run(screen,click,s_m_o_f)
	show_label(screen, 'B???n quy???n thu???c v??? B??? GD v?? ??T', font, (255,0,0), (1100,660))
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
	if y == 0:
		img = pygame.image.load(f'assets\\baigiang\\lop7\\bai{bai+1}.png').convert_alpha()
	else:
		img = pygame.image.load(f'assets\\baigiang\\lop7\\bai{bai+1}_{y}.png').convert_alpha()
	if 680-img.get_height()>0:
		scroll_y = 0
	elif scroll_y>0:
		scroll_y = 0
	elif scroll_y<680-img.get_height():
		scroll_y = 680-img.get_height()
	screen.blit(img,(200,scroll_y))
	back_to_class.run(screen,click,s_m_o_f)
	show_label(screen, 'B???n quy???n thu???c v??? B??? GD v?? ??T', font, (255,0,0), (1100,640))
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
	XO_text = ['??ang l?? l?????t c???a b???n, h??y ch???n m???t ??']
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
			show_label(screen,'H???c ch????ng tr??nh l???p 6',font,(0,0,0),(1280/2,660))
		if lop7_button.get_collide():
			show_label(screen,'H???c ch????ng tr??nh l???p 7',font,(0,0,0),(1280/2,660))
		if lop8_button.get_collide():
			show_label(screen,'H???c ch????ng tr??nh l???p 8',font,(0,0,0),(1280/2,660))
		if lop9_button.get_collide():
			show_label(screen,'H???c ch????ng tr??nh l???p 9',font,(0,0,0),(1280/2,660))
	elif lop6:
		if lop6_Dai_I:
			screen.blit(choose_class_bg,(-10,-10))
			back_button_to_l6.run(screen,click,s_m_o_f)
			for i in range(18):
				lop6_buttons_Dai_I[i].run(screen,click,s_m_o_f)
				if lop6_buttons_Dai_I[i].get_collide():
					if i == 0:
						show_label(screen,'B??i 1: T???P H???P, PH???N T??? C???A T???P H???P',font,(0,0,0),(640,630))
					elif i == 1:
						show_label(screen,'B??i 2: T???P H???P C??C S??? T??? NHI??N',font,(0,0,0),(640,630))
					elif i == 2:
						show_label(screen,'B??i 3: GHI S??? T??? NHI??N',font,(0,0,0),(640,630))
					elif i == 3:
						show_label(screen,'B??i 4: S??? PH???N T??? C???A T???P H???P. T???P H???P CON',font,(0,0,0),(640,630))
					elif i == 4:
						show_label(screen,'B??i 5: PH??P C???NG V?? PH??P NH??N',font,(0,0,0),(640,630))
					elif i == 5:
						show_label(screen,'B??i 6: PH??P TR??? V?? PH??P CHIA',font,(0,0,0),(640,630))
					elif i == 6:
						show_label(screen,'B??i 7: L??Y TH???A V???I S??? M?? T??? NHI??N. NH??N HAI L??Y TH???A C??NG C?? S???',font,(0,0,0),(640,630))
					elif i == 7:
						show_label(screen,'B??i 8: CHIA L??Y TH???A C??NG C?? S???',font,(0,0,0),(640,630))
					elif i == 8:
						show_label(screen,'B??i 9: TH??? T??? TH???C HI???N C??C PH??P T??NH',font,(0,0,0),(640,630))
					elif i == 9:
						show_label(screen,'B??i 10: T??NH CH???T CHIA H???T C???A M???T T???NG',font,(0,0,0),(640,630))
					elif i == 10:
						show_label(screen,f'B??i {i+1}: D???U HI???U CHIA H???T CHO 2, CHO 5',font,(0,0,0),(640,630))
					elif i == 11:
						show_label(screen,f'B??i {i+1}: D???U HI???U CHIA H???T CHO 3, CHO 9',font,(0,0,0),(640,630))
					elif i == 12:
						show_label(screen,f'B??i {i+1}: ?????C V?? B???I',font,(0,0,0),(640,630))
					elif i == 13:
						show_label(screen,f'B??i {i+1}: S??? NGUY??N T???. H???P S???. B???NG S??? NGUY??N T???',font,(0,0,0),(640,630))
					elif i == 14:
						show_label(screen,f'B??i {i+1}: PH??N T??CH RA TH???A S??? NGUY??N T???',font,(0,0,0),(640,630))
					elif i == 15:
						show_label(screen,f'B??i {i+1}: ?????C CHUNG V?? B???I CHUNG',font,(0,0,0),(640,630))
					elif i == 16:
						show_label(screen,f'B??i {i+1}: ?????C CHUNG L???N NH???T',font,(0,0,0),(640,630))
					elif i == 17:
						show_label(screen,f'B??i {i+1}: B???I CHUNG NH??? NH???T',font,(0,0,0),(640,630))

		elif lop6_Dai_II:
			screen.blit(choose_class_bg,(-10,-10))
			back_button_to_l6.run(screen,click,s_m_o_f)
			for i in range(13):
				lop6_buttons_Dai_II[i].run(screen,click,s_m_o_f)
				if lop6_buttons_Dai_II[i].get_collide():
					if i == 0:
						show_label(screen,f'B??i {i+1}: L??M QUEN V???I S??? NGUY??N ??M',font,(0,0,0),(640,630))
					elif i == 1:
						show_label(screen,f'B??i {i+1}: T???P H???P C??C S??? NGUY??N',font,(0,0,0),(640,630))
					elif i == 2:
						show_label(screen,f'B??i {i+1}: TH??? T??? TRONG T???P H???P C??C S??? NGUY??N',font,(0,0,0),(640,630))
					elif i == 3:
						show_label(screen,f'B??i {i+1}: C???NG HAI S??? NGUY??N C??NG D???U',font,(0,0,0),(640,630))
					elif i == 4:
						show_label(screen,f'B??i {i+1}: C???NG HAI S??? NGUY??N KH??C D???U',font,(0,0,0),(640,630))
					elif i == 5:
						show_label(screen,f'B??i {i+1}: T??NH CH???T C???A PH??P C???NG C??C S??? NGUY??N',font,(0,0,0),(640,630))
					elif i == 6:
						show_label(screen,f'B??i {i+1}: PH??P TR??? HAI S??? NGUY??N',font,(0,0,0),(640,630))
					elif i == 7:
						show_label(screen,f'B??i {i+1}: QUY T???C D???U NGO???C',font,(0,0,0),(640,630))
					elif i == 8:
						show_label(screen,f'B??i {i+1}: QUY T???C CHUY???N V???',font,(0,0,0),(640,630))
					elif i == 9:
						show_label(screen,f'B??i {i+1}: NH??N HAI S??? NGUY??N KH??C D???U',font,(0,0,0),(640,630))
					elif i == 10:
						show_label(screen,f'B??i {i+1}: NH??N HAI S?? NGUY??N C??NG D???U',font,(0,0,0),(640,630))
					elif i == 11:
						show_label(screen,f'B??i {i+1}: T??NH CH???T C???A PH??P NH??N',font,(0,0,0),(640,630))
					elif i == 12:
						show_label(screen,f'B??i {i+1}: B???I V?? ?????C C???A M???T S??? NGUY??N',font,(0,0,0),(640,630))

		elif lop6_Dai_III:
			screen.blit(choose_class_bg,(-10,-10))
			back_button_to_l6.run(screen,click,s_m_o_f)
			for i in range(17):
				lop6_buttons_Dai_III[i].run(screen,click,s_m_o_f)
				if lop6_buttons_Dai_III[i].get_collide():
					if i == 0:
						show_label(screen,f'B??i {i+1}: M??? R???NG KH??I NI???M PH??N S???',font,(0,0,0),(640,630))
					elif i == 1:
						show_label(screen,f'B??i {i+1}: PH??N S??? B???NG NHAU',font,(0,0,0),(640,630))
					elif i == 2:
						show_label(screen,f'B??i {i+1}: T??NH CH???T C?? B???N C???A PH??N S???',font,(0,0,0),(640,630))
					elif i == 3:
						show_label(screen,f'B??i {i+1}: R??T G???N PH??N S???',font,(0,0,0),(640,630))
					elif i == 4:
						show_label(screen,f'B??i {i+1}: QUY ?????NG M???U NHI???U PH??N S???',font,(0,0,0),(640,630))
					elif i == 5:
						show_label(screen,f'B??i {i+1}: SO S??NH PH??N S???',font,(0,0,0),(640,630))
					elif i == 6:
						show_label(screen,f'B??i {i+1}: PH??P C???NG PH??N S???',font,(0,0,0),(640,630))
					elif i == 7:
						show_label(screen,f'B??i {i+1}: T??NH CH???T C?? B???N C???A PH??P C???NG PH??N S???',font,(0,0,0),(640,630))
					elif i == 8:
						show_label(screen,f'B??i {i+1}: PH??P TR??? PH??N S???',font,(0,0,0),(640,630))
					elif i == 9:
						show_label(screen,f'B??i {i+1}: PH??P NH??N PH??N S???',font,(0,0,0),(640,630))
					elif i == 10:
						show_label(screen,f'B??i {i+1}: T??NH CH???T C?? B???N C???A PH??P NH??N PH??N S???',font,(0,0,0),(640,630))
					elif i == 11:
						show_label(screen,f'B??i {i+1}: PH??P CHIA PH??N S???',font,(0,0,0),(640,630))
					elif i == 12:
						show_label(screen,f'B??i {i+1}: H???N S???. S??? TH???P PH??N. PH???N TR??M',font,(0,0,0),(640,630))
					elif i == 13:
						show_label(screen,f'B??i {i+1}: T??M GI?? TR??? PH??N S??? C???A M???T S??? CHO TR?????C',font,(0,0,0),(640,630))
					elif i == 14:
						show_label(screen,f'B??i {i+1}: T??M M???T S??? BI???T GI?? TR??? C???A M???T PH??N S??? C???A N??',font,(0,0,0),(640,630))
					elif i == 15:
						show_label(screen,f'B??i {i+1}: T??M T??? S??? C???A HAI S???',font,(0,0,0),(640,630))
					elif i == 16:
						show_label(screen,f'B??i {i+1}: BI???U ????? PH???N TR??M',font,(0,0,0),(640,630))

		elif lop6_Hinh_I:
			screen.blit(choose_class_bg,(-10,-10))
			back_button_to_l6.run(screen,click,s_m_o_f)
			for i in range(10):
				lop6_buttons_Hinh_I[i].run(screen,click,s_m_o_f)
				if lop6_buttons_Hinh_I[i].get_collide():
					if i == 0:
						show_label(screen,f'B??i {i+1}: ??I???M. ???????NG TH???NG',font,(0,0,0),(640,630))
					elif i == 1:
						show_label(screen,f'B??i {i+1}: BA ??I???M TH???NG H??NG',font,(0,0,0),(640,630))
					elif i == 2:
						show_label(screen,f'B??i {i+1}: ???????NG TH???NG ??I QUA HAI ??I???M',font,(0,0,0),(640,630))
					elif i == 3:
						show_label(screen,f'B??i {i+1}: TH???C H??NH (KH??NG C?? L?? THUY???T)',font,(0,0,0),(640,630))
					elif i == 4:
						show_label(screen,f'B??i {i+1}: TIA',font,(0,0,0),(640,630))
					elif i == 5:
						show_label(screen,f'B??i {i+1}: ??O???N TH???NG',font,(0,0,0),(640,630))
					elif i == 6:
						show_label(screen,f'B??i {i+1}: ????? D??I ??O???N TH???NG',font,(0,0,0),(640,630))
					elif i == 7:
						show_label(screen,f'B??i {i+1}: KHI N??O TH?? AM + MB = AB ?',font,(0,0,0),(640,630))
					elif i == 8:
						show_label(screen,f'B??i {i+1}: V??? ??O???N TH???NG CHO BI???T ????? D??I',font,(0,0,0),(640,630))
					elif i == 9:
						show_label(screen,f'B??i {i+1}: TRUNG ??I???M C???A ??O???N TH???NG',font,(0,0,0),(640,630))
					

		elif lop6_Hinh_II:
			screen.blit(choose_class_bg,(-10,-10))
			back_button_to_l6.run(screen,click,s_m_o_f)
			for i in range(9):
				lop6_buttons_Hinh_II[i].run(screen,click,s_m_o_f)
				if lop6_buttons_Hinh_II[i].get_collide():
					if i == 0:
						show_label(screen,f'B??i {i+1}: N???A M???T PH???NG',font,(0,0,0),(640,630))
					elif i == 1:
						show_label(screen,f'B??i {i+1}: G??C',font,(0,0,0),(640,630))
					elif i == 2:
						show_label(screen,f'B??i {i+1}: S??? ??O G??C',font,(0,0,0),(640,630))
					elif i == 3:
						show_label(screen,f'B??i {i+1}: KHI N??O TH?? xOy + yOz = xOz?',font,(0,0,0),(640,630))
					elif i == 4:
						show_label(screen,f'B??i {i+1}: V??? G??C CHO BI???T S??? ??O',font,(0,0,0),(640,630))
					elif i == 5:
						show_label(screen,f'B??i {i+1}: TIA PH??N GI??C C???A G??C',font,(0,0,0),(640,630))
					elif i == 6:
						show_label(screen,f'B??i {i+1}: TH???C H??NH',font,(0,0,0),(640,630))
					elif i == 7:
						show_label(screen,f'B??i {i+1}: ???????NG TR??N',font,(0,0,0),(640,630))
					elif i == 8:
						show_label(screen,f'B??i {i+1}: TAM GI??C',font,(0,0,0),(640,630))
		elif XO_l6:
			screen.blit(XO_bg,(0,0))
			if XO_wait:
				if XO_O[0] == XO_O[1] == XO_O[2] == 'O' or XO_O[3] == XO_O[4] == XO_O[5] == 'O' or XO_O[6] == XO_O[7] == XO_O[8] == 'O' or XO_O[0] == XO_O[3] == XO_O[6] == 'O' or XO_O[1] == XO_O[4] == XO_O[7] == 'O' or XO_O[2] == XO_O[5] == XO_O[8] == 'O' or XO_O[0] == XO_O[4] == XO_O[8] == 'O' or XO_O[2] == XO_O[4] == XO_O[6] == 'O':
					XO_win = True
					XO_wait = False
					XO_text.append('Ch??c m???ng, b???n ???? chi???n th???ng!!')
					
				elif XO_O[0] == XO_O[1] == XO_O[2] == 'X' or XO_O[3] == XO_O[4] == XO_O[5] == 'X' or XO_O[6] == XO_O[7] == XO_O[8] == 'X' or XO_O[0] == XO_O[3] == XO_O[6] == 'X' or XO_O[1] == XO_O[4] == XO_O[7] == 'X' or XO_O[2] == XO_O[5] == XO_O[8] == 'X' or XO_O[0] == XO_O[4] == XO_O[8] == 'X' or XO_O[2] == XO_O[4] == XO_O[6] == 'X':
					XO_lose = True
					XO_wait = False
					XO_text.append('M??y t??nh ???? chi???n th???ng, ch??c b???n may m???n l???n sau')
				if XO_turn == 'c':
					XO_turn = 'p'
					XO_ingenerate = True
					while XO_ingenerate:
						XO_c_pick = random.randint(0,8)
						if XO_O[XO_c_pick] == 'n':
							XO_O[XO_c_pick] = 'X'
							XO_ingenerate = False
							time.sleep(1)
							XO_text.append(f'<c>M??y t??nh ch???n ?? s??? {XO_c_pick}           ')
							XO_text.append('<o>L?????t c???a b???n, h??y ch???n m???t ??:         ')

				for i in range(9):
					if XO_O[i] == 'n':
						mouse_pos = pygame.mouse.get_pos()
						if XO_rect[i].collidepoint(mouse_pos):
							XO_index[i] = 1
							if click and pygame.mouse.get_pressed()[0]:
								XO_selected = i
								XO_wait = False
								s_m_o_f()
								XO_text.append(f'<o>???? ch???n ?? {i}                ')
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
					XO_text.append('<o> H??y tr??? l???i c??u h???i ????? t??ch "O"       ')
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
						XO_text.append('<o> B???n ???? tr??? l???i ch??nh x??c, ???? ????nh d???u!')
					elif XO_AnsButton[i].get_return() != XO_RAP and XO_AnsButton[i].get_return() != None:
						XO_selected = None
						XO_wait = True
						XO_text.append('<!> Th??i, sai m???t r???i :(                  ')

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
								XO_text.append(f'<o>???? ch???n ?? {i}                ')
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
					XO_text = ['??ang l?? l?????t c???a b???n, h??y ch???n m???t ??']
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
								XO_text.append(f'<o>???? ch???n ?? {i}                ')
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
					XO_text = ['??ang l?? l?????t c???a b???n, h??y ch???n m???t ??']
			
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
				show_label(screen,'CH????NG I: ??N T???P V?? B??? T??C KI???N TH???C V??? S??? T??? NHI??N',font,(0,0,0),(640,630))
			if Chuong_I_Hinh_Button.get_collide():
				show_label(screen,'CH????NG I: ??O???N TH???NG',font,(0,0,0),(640,630))
			if Chuong_II_Dai_Button.get_collide():
				show_label(screen,'CH????NG II: S??? NGUY??N',font,(0,0,0),(640,630))
			if Chuong_II_Hinh_Button.get_collide():
				show_label(screen,'CH????NG II: PH??N S???',font,(0,0,0),(640,630))
			if Chuong_III_Dai_Button.get_collide():
				show_label(screen,'CH????NG III: G??C',font,(0,0,0),(640,630))
	elif lop7:
		if lop7_Dai_I:
			screen.blit(choose_class_bg,(-10,-10))
			back_button_to_l7.run(screen,click,s_m_o_f)
			for i in range(12):
				lop7_buttons_Dai_I[i].run(screen,click,s_m_o_f)
				if lop7_buttons_Dai_I[i].get_collide():
					if i == 0:
						show_label(screen, f'B??I {i+1}: T???P H???P Q C??C S??? H???U T???', font, (0,0,0), (640,630))
					elif i == 1:
						show_label(screen, f'B??I {i+1}: C???NG TR??? S??? H???U T???', font, (0,0,0), (640,630))
					elif i == 2:
						show_label(screen, f'B??I {i+1}: NH??N, CHIA C??C S??? H???U T???', font, (0,0,0), (640,630))
					elif i == 3:
						show_label(screen, f'B??I {i+1}: GI?? TR??? TUY???T ?????I C???A M???T S?? H???U T???. C???NG, TR???, NH??N CHIA S??? TH???P PH??N', font, (0,0,0), (640,630))
					elif i == 4:
						show_label(screen, f'B??I {i+1}: L??Y TH???A C???A M???T S??? H???U T???', font, (0,0,0), (640,630))
					elif i == 5:
						show_label(screen, f'B??I {i+1}: L??Y TH???A C???A M???T S??? H???U T??? (TI???P)', font, (0,0,0), (640,630))
					elif i == 6:
						show_label(screen, f'B??I {i+1}: T??? L??? TH???C', font, (0,0,0), (640,630))
					elif i == 7:
						show_label(screen, f'B??I {i+1}: T??NH CH???T C???A D??Y T??? S??? B???NG NHAU', font, (0,0,0), (640,630))
					elif i == 8:
						show_label(screen, f'B??I {i+1}: S??? TH???P PH??N H???U H???N. S??? TH???P PH??N V?? H???N TU???N HO??N', font, (0,0,0), (640,630))
					elif i == 9:
						show_label(screen, f'B??I {i+1}: L??M TR??N S???', font, (0,0,0), (640,630))
					elif i == 10:
						show_label(screen, f'B??I {i+1}: S??? V?? T???. KH??I NI???M V??? C??N B???C HAI', font, (0,0,0), (640,630))
					elif i == 11:
						show_label(screen, f'B??I {i+1}: S??? TH???C', font, (0,0,0), (640,630))
		elif lop7_Dai_II:
			screen.blit(choose_class_bg,(-10,-10))
			back_button_to_l7.run(screen,click,s_m_o_f)
			for i in range(7):
				lop7_buttons_Dai_II[i].run(screen,click,s_m_o_f)
				if lop7_buttons_Dai_II[i].get_collide():
					if i == 0:
						show_label(screen, f'B??I {i+1}: ?????I L?????NG T??? L??? THU???N', font, (0,0,0), (640,630))
					elif i == 1:
						show_label(screen, f'B??I {i+1}: M???T S??? B??I TO??N V??? ?????I L?????NG T??? L??? THU???N', font, (0,0,0), (640,630))
					elif i == 2:
						show_label(screen, f'B??I {i+1}: ?????I L?????NG T??? L??? NGH???CH', font, (0,0,0), (640,630))
					elif i == 3:
						show_label(screen, f'B??I {i+1}: M???T S??? B??I TO??N V??? ?????I L?????NG T??? L??? NGH???CH', font, (0,0,0), (640,630))
					elif i == 4:
						show_label(screen, f'B??I {i+1}: H??M S???', font, (0,0,0), (640,630))
					elif i == 5:
						show_label(screen, f'B??I {i+1}: M???T PH???NG T???A ?????', font, (0,0,0), (640,630))
					elif i == 6:
						show_label(screen, f'B??I {i+1}: ????? TH??? H??M S??? y = ax (a kh??c 0)', font, (0,0,0), (640,630))
		elif lop7_Dai_III:
			screen.blit(choose_class_bg,(-10,-10))
			back_button_to_l7.run(screen,click,s_m_o_f)
			for i in range(4):
				lop7_buttons_Dai_III[i].run(screen,click,s_m_o_f)
				if lop7_buttons_Dai_III[i].get_collide():
					if i == 0:
						show_label(screen, f'B??I {i+1}: THU TH???P S??? LI???U TH???NG K??, T???N S???', font, (0,0,0), (640,630))
					elif i == 1:
						show_label(screen, f'B??I {i+1}: B???NG "T???N S???" C??C GI?? TR??? C???A D???U HI???U*', font, (0,0,0), (640,630))
					elif i == 2:
						show_label(screen, f'B??I {i+1}: BI???U ?????', font, (0,0,0), (640,630))
					elif i == 3:
						show_label(screen, f'B??I {i+1}: S??? TRUNG B??NH C???NG', font, (0,0,0), (640,630))
		elif lop7_Dai_IV:
			screen.blit(choose_class_bg,(-10,-10))
			back_button_to_l7.run(screen,click,s_m_o_f)
			for i in range(9):
				lop7_buttons_Dai_IV[i].run(screen,click,s_m_o_f)
				if lop7_buttons_Dai_IV[i].get_collide():
					if i == 0:
						show_label(screen, f'B??I {i+1}: KH??I NI???M V??? BI???U TH???C ?????I S???', font, (0,0,0), (640,630))
					elif i == 1:
						show_label(screen, f'B??I {i+1}: GI?? TR??? C???A M???T BI???U TH???C ?????I S???', font, (0,0,0), (640,630))
					elif i == 2:
						show_label(screen, f'B??I {i+1}: ????N TH???C', font, (0,0,0), (640,630))
					elif i == 3:
						show_label(screen, f'B??I {i+1}: ????N TH???C ?????NG D???NG', font, (0,0,0), (640,630))
					elif i == 4:
						show_label(screen, f'B??I {i+1}: ??A TH???C', font, (0,0,0), (640,630))
					elif i == 5:
						show_label(screen, f'B??I {i+1}: C???NG, TR??? ??A TH???C', font, (0,0,0), (640,630))
					elif i == 6:
						show_label(screen, f'B??I {i+1}: ??A TH???C M???T BI???N', font, (0,0,0), (640,630))
					elif i == 7:
						show_label(screen, f'B??I {i+1}: C???NG TR??? ??A TH???C M???T BI???N', font, (0,0,0), (640,630))
					elif i == 8:
						show_label(screen, f'B??I {i+1}: NGHI???M C???A ??A TH???C M???T BI???N', font, (0,0,0), (640,630))
		elif lop7_Hinh_I:
			screen.blit(choose_class_bg,(-10,-10))
			back_button_to_l7.run(screen,click,s_m_o_f)
			for i in range(7):
				lop7_buttons_Hinh_I[i].run(screen,click,s_m_o_f)
				if lop7_buttons_Hinh_I[i].get_collide():
					if i == 0:
						show_label(screen, f'B??I {i+1}: HAI G??C ?????I ?????NH', font, (0,0,0), (640,630))
					elif i == 1:
						show_label(screen, f'B??I {i+1}: HAI ???????NG TH???NG VU??NG G??C', font, (0,0,0), (640,630))
					elif i == 2:
						show_label(screen, f'B??I {i+1}: C??C G??C T???O B???I M???T ???????NG TH???NG C???T HAI ???????NG TH???NG', font, (0,0,0), (640,630))
					elif i == 3:
						show_label(screen, f'B??I {i+1}: HAI ???????NG TH???NG SONG SONG', font, (0,0,0), (640,630))
					elif i == 4:
						show_label(screen, f'B??I {i+1}: TI??N ????? ??-CLIT V??? ???????NG TH???NG SONG SONG', font, (0,0,0), (640,630))
					elif i == 5:
						show_label(screen, f'B??I {i+1}: T??? VU??NG G??C ?????N SONG SONG', font, (0,0,0), (640,630))
					elif i == 6:
						show_label(screen, f'B??I {i+1}: ?????NH L??', font, (0,0,0), (640,630))
		elif lop7_Hinh_II:
			screen.blit(choose_class_bg,(-10,-10))
			back_button_to_l7.run(screen,click,s_m_o_f)
			for i in range(9):
				lop7_buttons_Hinh_II[i].run(screen,click,s_m_o_f)
				if lop7_buttons_Hinh_II[i].get_collide():
					if i == 0:
						show_label(screen, f'B??I {i+1}: T???NG BA G??C C???A TAM GI??C', font, (0,0,0), (640,630))
					elif i == 1:
						show_label(screen, f'B??I {i+1}: HAI TAM GI??C B???NG NHAU', font, (0,0,0), (640,630))
					elif i == 2:
						show_label(screen, f'B??I {i+1}: TR?????NG H???P B???NG NHAU TH??? NH???T C???A TAM GI??C. C???NH - C???NH - C???NH (c.c.c)', font, (0,0,0), (640,630))
					elif i == 3:
						show_label(screen, f'B??I {i+1}: TR?????NG H???P B???NG NHAU TH??? HAI C???A TAM GI??C. C???NH - G??C - C???NH (c.g.c)', font, (0,0,0), (640,630))
					elif i == 4:
						show_label(screen, f'B??I {i+1}: TR?????NG H???P B???NG NHAU TH??? BA C???A TAM GI??C. G??C - C???NH - G??C (g.c.g)', font, (0,0,0), (640,630))
					elif i == 5:
						show_label(screen, f'B??I {i+1}: TAM GI??C C??N', font, (0,0,0), (640,630))
					elif i == 6:
						show_label(screen, f'B??I {i+1}: ?????NH L?? Pi-ta-go', font, (0,0,0), (640,630))
					elif i == 7:
						show_label(screen, f'B??I {i+1}: C??C TR?????NG H???P B???NG NHAU C???A TAM GI??C VU??NG', font, (0,0,0), (640,630))
					elif i == 8:
						show_label(screen, f'B??I {i+1}: TH???C H??NH NGO??I TR???I', font, (0,0,0), (640,630))
		elif lop7_Hinh_III:
			screen.blit(choose_class_bg,(-10,-10))
			back_button_to_l7.run(screen,click,s_m_o_f)
			for i in range(9):
				lop7_buttons_Hinh_III[i].run(screen,click,s_m_o_f)
				if lop7_buttons_Hinh_III[i].get_collide():
					if i == 0:
						show_label(screen, f'B??I {i+1}: QUAN H??? GI???A G??C V?? C???NH ?????I DI???N TRONG M???T TAM GI??C', font, (0,0,0), (640,630))
					elif i == 1:
						show_label(screen, f'B??I {i+1}: QUAN H??? GI???A ???????NG VU??NG G??C V?? ???????NG XI??N, ???????NG XI??N V?? H??NH CHI???U', font, (0,0,0), (640,630))
					elif i == 2:
						show_label(screen, f'B??I {i+1}: QUAN H??? GI???A C??C C???NH C???A M???T TAM GI??C. B???T ?????NG TH???C TAM GI??C', font, (0,0,0), (640,630))
					elif i == 3:
						show_label(screen, f'B??I {i+1}: T??NH CH???T BA ???????NG TRUNG TUY???N C???A TAM GI??C', font, (0,0,0), (640,630))
					elif i == 4:
						show_label(screen, f'B??I {i+1}: T??NH CH???T TIA PH??N GI??C C???A M???T G??C', font, (0,0,0), (640,630))
					elif i == 5:
						show_label(screen, f'B??I {i+1}: T??NH CH???T BA ???????NG PH??N GI??C C???A TAM GI??C', font, (0,0,0), (640,630))
					elif i == 6:
						show_label(screen, f'B??I {i+1}: T??NH CH???T ???????NG TRUNG TR???C C???A M???T ??O???N TH???NG', font, (0,0,0), (640,630))
					elif i == 7:
						show_label(screen, f'B??I {i+1}: T??NH CH???T BA ???????NG TRUNG TR???C C???A TAM GI??C', font, (0,0,0), (640,630))
					elif i == 8:
						show_label(screen, f'B??I {i+1}: T??NH CH???T BA ???????NG CAO C???A TAM GI??C', font, (0,0,0), (640,630))
		elif CM_l7:
			if CM_ingenerate:
				for i in range(6):
					CM_t = ''
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

				CM_question = f'Cho ??a th???c {CM_tvar[0]}x{CM_tvar[1]}xy{CM_tvar[2]}y{CM_tvar[3]}x{CM_tvar[4]}y{CM_tvar[5]} . H??y t??m h??? s??? c???a {CM_WTFind}.'
				CM_ingenerate = False
			screen.blit(CM_bg,(0,0))
			for i in range(10):
				CM_buttons[i].run(screen,click,s_m_o_f)
			show_label_topleft(screen,CM_question,font,(0,0,0),(78,55))
			show_label_topleft(screen,get_CM_t(),font,(0,0,0),(78,75))
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
				show_label(screen,'CH????NG I: S??? H???U T???. S??? TH???C',font,(0,0,0),(1280/2,660))
			elif Chuong_II_Dai_Button.get_collide():
				show_label(screen,'CH????NG II: H??M S??? V?? ????? TH???',font,(0,0,0),(1280/2,660))
			elif Chuong_III_Dai_Button.get_collide():
				show_label(screen,'CH????NG III: TH???NG K??',font,(0,0,0),(1280/2,660))
			elif Chuong_IV_Dai_Button.get_collide():
				show_label(screen,'CH????NG IV: BI???U TH???C ?????I S???',font,(0,0,0),(1280/2,660))
			elif Chuong_I_Hinh_Button.get_collide():
				show_label(screen,'CH????NG I: ???????NG TH???NG VU??NG G??C',font,(0,0,0),(1280/2,660))
			elif Chuong_II_Hinh_Button.get_collide():
				show_label(screen,'CH????NG II: TAM GI??C',font,(0,0,0),(1280/2,660))
			elif Chuong_III_Hinh_Button.get_collide():
				show_label(screen,'CH????NG III: QUAN H??? GI???A C??C Y???U T??? TRONG TAM GI??C. C??C ???????NG ?????NG QUY C???A TAM GI??C',font,(0,0,0),(1280/2,700))
	elif lop8:
		screen.fill((255,255,255))
		back_button_to_sc8.run(screen,click,s_m_o_f)
		img = font.render('Ch??a c???p nh???t :(', True, (0,0,0))
		screen.blit(img,(100,100))
	elif lop9:
		screen.fill((255,255,255))
		back_button_to_sc9.run(screen,click,s_m_o_f)
		img = font.render('Ch??a c???p nh???t :(', True, (0,0,0))
		screen.blit(img,(100,100))
	elif setting:
		screen.fill((255,255,255))
		back_button_to_sc.run(screen,click,s_m_o_f)




	if pygame.mouse.get_pressed()[0] == False and can_c==False:
		can_c = True


	pygame.display.update()
	clock.tick(60)
	check_quit()