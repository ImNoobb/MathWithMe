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


# X O Games ============================================== #
XO_running = True
XO_wait = True
XO_O = ['n','n','n','n','n','n','n','n','n']