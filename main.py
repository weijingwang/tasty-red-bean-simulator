import pygame
import random
from datetime import datetime
pygame.mixer.pre_init()
pygame.init()
pygame.mixer.music.load("./assets/music/red-planet_compress.ogg")
pygame.mixer.music.play(-1,0.0)
pygame.mixer.music.set_volume(0.5)

# pygame.mouse.set_visible(False)

screen = pygame.display.set_mode((1280, 720))

bg = pygame.image.load("./assets/bg.png").convert_alpha()
bg = pygame.transform.scale(bg,(960,720))

pot = pygame.image.load("./assets/pot.png").convert_alpha()
pot = pygame.transform.scale(pot,(200,200))
pot_rect = pot.get_rect()

current_hour = int(datetime.now().strftime("%H"))

done = False
clock = pygame.time.Clock()

class ParticlePrinciple:
	def __init__(self):
		self.particles = []

	def emit(self):
		if self.particles:
			self.delete_particles()
			for particle in self.particles:
				particle[0][1] += particle[2][0]
				particle[0][0] += particle[2][1]
				particle[1] -= 0.2
				pygame.draw.circle(screen,pygame.Color(152,219,221),particle[0], int(particle[1]))

	def add_particles(self):
		pos_x = pygame.mouse.get_pos()[0]
		pos_y = pygame.mouse.get_pos()[1] 
		radius = 10
		direction_x = random.randint(-3,3)
		direction_y = random.randint(-3,3)
		particle_circle = [[pos_x,pos_y],radius,[direction_x,direction_y]]
		self.particles.append(particle_circle)

	def delete_particles(self):
		particle_copy = [particle for particle in self.particles if particle[1] > 0]
		self.particles = particle_copy


class KitchenThings(pygame.sprite.Sprite):
	def __init__(self,image_link,coords, display,kind,width,height):
		super().__init__()
		self.image_link=image_link
		self.display = display
		self.coords = coords
		self.image = pygame.image.load(self.image_link).convert_alpha()
		self.image = pygame.transform.scale(self.image, (width, height))
		self.image_og = self.image
		self.image_big = pygame.transform.scale(self.image, (width+50, height+50))

		self.rect =self.image.get_rect()
		self.rect.center = self.coords
		self.coords_og = self.coords
		self.kind = kind

		self.can_activate = True

		self.status = 0

		self.sfx =pygame.mixer.Sound("./assets/music/sound/CLICK_SMALL.ogg")



	def Draw(self,active,mouse_pos):
		
		if active==True and self.rect.collidepoint(mouse_pos):
			self.display.blit(self.image_big,self.rect)

			if self.can_activate==True:
				pygame.mixer.Sound.play(self.sfx)
				self.can_activate = False
				return self.kind
	
		else:
			self.can_activate=True
			self.display.blit(self.image,self.rect)


class Customer(pygame.sprite.Sprite):
	"""docstring for ClassName"""
	def __init__(self, display):
		super().__init__()
		self.display = display

		self.images = []
		self.images.append(pygame.image.load('./assets/customer.png').convert_alpha())
		self.images.append(pygame.image.load('./assets/customer_happy.png').convert_alpha())
		self.images.append(pygame.image.load('./assets/customer_angry.png').convert_alpha())

		self.image = self.images[0]
		self.rect = self.image.get_rect()
		self.rect.bottomleft = 1280,720
		self.go_up = True
		self.bottomleft_comp = [1280,720]
		self.accel = 0
		self.velocity = 50
	def Render(self):
		self.display.blit(self.image,self.rect)
	def Update(self):

		# print(self.bottomleft_comp)
		self.rect.bottomleft = self.bottomleft_comp
		# print(self.rect.bottom)


	def Move(self,status,order_correct):#0: incoming, 1: wait, 2: leaving
		# print(status)
		if status == 0:
			self.image = self.images[0]
			# self.accel=1
			if self.bottomleft_comp[0]>570:
				self.bottomleft_comp[0] -=self.velocity
				# self.velocity-=self.accel
				return 0
			if self.rect.left == 530:
				print(self.bottomleft_comp[0])
				return 1

		


		if self.go_up ==True and self.bottomleft_comp[1] > 690:
			self.bottomleft_comp[1] -=0.5
		if self.bottomleft_comp[1] == 690:
			self.go_up=False
		if self.bottomleft_comp[1] < 730 and self.go_up == False:
			self.bottomleft_comp[1] +=0.5
		if self.bottomleft_comp[1]==730:
			self.go_up=True

		if status==1:
			return 1
			print('wait')




		if status ==2:
			if order_correct==True:
				self.image = self.images[1]
			else:
				self.image = self.images[2]
			if self.bottomleft_comp[0]>-400:
				self.bottomleft_comp[0]-=self.velocity
				return 2
			if self.bottomleft_comp[0]<=-400:
				print('gfhjgh')
				self.rect.bottomleft = 1280,720
				self.bottomleft_comp = [1280,720]
				return 0
		print(self.rect)


		

		# if self.rect.bottom< 521:
		# 	self.rect.move_ip(0,-1)
		# elif self.rect.bottom510:
		# 	self.rect.move_ip(0,1)

	def CheckOrder(self):
		pass





RedBeans = KitchenThings("./assets/red_beans.png",(150,150),screen,'beans',200,200)
Sugar = KitchenThings("./assets/sugar.png",(150,400),screen,'sugar',200,200)
Water = KitchenThings("./assets/water.png",(800,590),screen,'water',325,195)
Heat = KitchenThings("./assets/heat.png",(1150,650),screen,'heat',213,114)

CustomerTest = Customer(screen)


my_order = [0,0,0,0]
customer_order = [2,1,1,0]
#beans,sugar,water,heat

order_correct = False

side_bar_color = 'black'


particle1 = ParticlePrinciple()
PARTICLE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(PARTICLE_EVENT,40)


customer_status = 0



#FADERS=======

finished_dish1 = pygame.image.load("./assets/Red_Bean_Soup.png").convert_alpha()
finished_dish1.set_alpha(0)
alph = 0
fading = False
show_beans=False



SCORE = 0



#SOUND++++++++++++++++
ANGER = pygame.mixer.Sound("./assets/music/sound/ANGER.ogg")
OK_SOUND = pygame.mixer.Sound("./assets/music/sound/CLICK.ogg")

while not done:


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quit()
		if event.type == PARTICLE_EVENT:
			particle1.add_particles()

	mouse_pos = pygame.mouse.get_pos()
	mouse_press = pygame.mouse.get_pressed()[0]


	if current_hour>=7 and current_hour<=11:
		# print('morning')
		screen.fill((215,232,253))
		side_bar_color= (111,153,64)

	elif current_hour>=12 and current_hour<=17:
		screen.fill((170,196,201))
		side_bar_color = (99,119,91)
		# print('noon')
	else:
		screen.fill((48,64,90))
		side_bar_color=(115,112,0)
		# print('night')

	screen.blit(bg,(320,0))
	pygame.draw.rect(screen, side_bar_color, pygame.Rect(0, 0, 320, 720))
	bean_counter = RedBeans.Draw(mouse_press,mouse_pos)
	sugar_counter = Sugar.Draw(mouse_press,mouse_pos)


	CustomerTest.Render()
	customer_status_output = CustomerTest.Move(customer_status,order_correct)
	customer_status = customer_status_output
	CustomerTest.Update()


	pygame.draw.rect(screen, (170,135,54), pygame.Rect(0, 570, 1280, 150))

	water_counter = Water.Draw(mouse_press,mouse_pos)
	heat_counter = Heat.Draw(mouse_press,mouse_pos)
	screen.blit(pot,(300,500))


	finished_dish1.set_alpha(alph)
	screen.blit(finished_dish1,(0,0))


	# print(customer_status_output)




	# print(show_beans)

	if bean_counter =='beans':
		my_order[0]+=1
	elif sugar_counter =='sugar':
		my_order[1]+=1
	elif water_counter =='water':
		my_order[2]+=1
	elif heat_counter =='heat':
		my_order[3]+=1



	if my_order == customer_order:
		pygame.mixer.Sound.play(OK_SOUND)
		order_correct=True
		customer_status = 2
		show_beans = True
		my_order = [0,0,0,0]
		SCORE +=1
		print('score is '+str(SCORE))



	if sum(my_order) > sum(customer_order):
		pygame.mixer.Sound.play(ANGER)
		customer_status = 2
		order_correct=False
		my_order = [0,0,0,0]
		print('reset order')

	if show_beans==True and fading==False:
		fading=False
		print('coming')
		if alph <= 500:
			alph+=40
		if alph >=500:
			fading = True
			print('false')
			show_beans=False
	if fading==True:
		print('fading')
		alph-=40
		if alph<=0:
			fading =False
	print(alph)

	# print(my_order)

	particle1.emit()
	clock.tick(30)
	pygame.display.flip()