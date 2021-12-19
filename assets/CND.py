import pygame,random
from pygame.locals import *

class A_Button():
	def __init__(self, button_list,speed,pos,cmd):
		self.button_img = button_list
		self.speed = speed
		self.index = 0
		self.rect = self.button_img[0].get_rect(topleft=pos)
		self.cmd = cmd
		self.collide = False

	def run(self,scr,click,s_m_o_f):
		mouse_pos = pygame.mouse.get_pos()
		if self.rect.collidepoint(mouse_pos):
			self.collide = True
			self.index += self.speed
			if int(self.index) > len(self.button_img)-1:
				self.index = len(self.button_img)-1
			if click and pygame.mouse.get_pressed()[0]:
				self.cmd()
				s_m_o_f()
		elif not self.rect.collidepoint(mouse_pos):
			self.collide = False
			self.index -= self.speed
			if int(self.index) < 0:
				self.index = 0

		scr.blit(self.button_img[int(self.index)],self.rect)

	def set_index(self,index):
		self.index = index

	def get_collide(self):
		return self.collide

class N_Button():
	def __init__(self,btn_img,btn_img_hover,pos,cmd):
		self.button = [btn_img,btn_img_hover]
		self.rect = self.button[0].get_rect(topleft=pos)
		self.cmd = cmd
		self.index = 0
		self.col = False
		self.get_pressed = None

	def run(self,scr,click,s_m_o_f):
		mouse_pos = pygame.mouse.get_pos()
		if self.rect.collidepoint(mouse_pos):
			self.col = True
			self.index = 1
			if click and pygame.mouse.get_pressed()[0]:
				self.cmd()
				s_m_o_f()
				self.get_pressed = True
		else:
			self.index = 0
			self.col = False

		scr.blit(self.button[self.index],self.rect)

	def change_cmd(self,cmd):
		self.cmd = cmd

	def get_collide(self):
		return self.col

	def get_cmd(self):
		return self.cmd

	def get_pressed_now(self):
		return self.get_pressed

def show_label(scr,text,font,color,center_pos):
	img = font.render(text, True, color)
	rect = img.get_rect(center = center_pos)
	scr.blit(img,rect)

class T_Button():
	def __init__(self,btn_img,btn_img_hover,pos,varibles_return,font):
		self.button = [btn_img,btn_img_hover]
		self.rect = self.button[0].get_rect(topleft=pos)
		self.cmd = cmd
		self.index = 0
		self.text = ''
		self.text_img = font.render(self.text, True ,(0,0,0))
		self.text_rect = self.text_img.get_rect(center = self.rect.center)
		self.varibles_return = varibles_return

	def run(self,scr,click,s_m_o_f):
		mouse_pos = pygame.mouse.get_pos()
		if self.rect.collidepoint(mouse_pos):
			self.index = 1
			if click and pygame.mouse.get_pressed()[0]:
				s_m_o_f()
				return self.varibles_return
				print('RETURNED')
		else:
			self.index = 0
			self.col = False

		scr.blit(self.button[self.index],self.rect)

	def set_text(self,text):
		self.text = text
		self.text_img = font.render(self.text, True ,(0,0,0))
		self.text_rect = self.text_img.get_rect(center = self.rect.center)


# X O Games ============================================== #
XO_font = pygame.font.Font(None,15)
XO_selected = None
def set_selected(which):
	global XO_selected,XO_wait
	XO_selected = which
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
	temp = T_Button(temp1,temp2,font)

