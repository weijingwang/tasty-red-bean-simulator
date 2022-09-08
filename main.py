import pygame
import random
from datetime import datetime
pygame.mixer.pre_init()
pygame.init()
pygame.display.set_caption("Tasty Red Bean Simulator (Pyweek34)")
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

pygame.mixer.music.load("./assets/music/red-planet_compress.ogg")
pygame.mixer.music.play(-1,0.0)
pygame.mixer.music.set_volume(0.5)

#beans,sugar,water,heat
# menu = [Red_Bean_Soup,	Beans_Cup,	Sugar_Cup,	Sugar_Water,	Water_Cup,	Nothing]
def order_image(order):
	if order[0]!=0 and order[1]!=0 and order[2]!=0:
		print(order)
		print('red bean soup')
		return 0
	if order[0]!=0 and order[1]==0 and order[2]!=0:
		print(order)
		print('red bean soup (no sugar)')
		return 0

	if order[0]!=0 and order[1]==0 and order[2]==0:
		print(order)
		print('bean cup')
		return 1
	if order[0]!=0 and order[1]!=0 and order[2]==0:
		print(order)
		print('bean cup (w/ sugar)')
		return 1

	if order[0]==0 and order[1]!=0 and order[2]==0:
		print(order)
		print('sugar cup')
		return 2

	if order[0]==0 and order[1]!=0 and order[2]!=0:
		print(order)
		print('sugar water')
		return 3


	if order[0]==0 and order[1]==0 and order[2]!=0:
		print(order)
		print('water cup')
		return 4


	if order[0]==0 and order[1]==0 and order[2]==0:
		print(order)
		print('Nothing')
		return 5

class Text(pygame.sprite.Sprite):
    def __init__(self,screen,message,pos,size,bottom) -> None:
        super().__init__()
        self.screen = screen
        self.pos = pos
        self.size = size
        self.bottom = bottom
        self.original_size = self.size
        self.color=(200,200,200)
        self.myFont = pygame.font.Font("./assets/font/Ubuntu-Title.ttf", self.size)
        self.message = message
        self.image = self.myFont.render(self.message, 1, self.color)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        
    def update(self,on):
        self.rect.center = self.pos
        if on==True:
            self.color = (250,200,200)
        elif on==False:
            self.color = (70,67,78)
        if self.bottom == True:
            self.color = (250,200,200)
        self.image = self.myFont.render(self.message, 1, self.color)


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
				# print(self.bottomleft_comp[0])
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
			# print('wait')




		if status ==2:
			if order_correct==True:
				self.image = self.images[1]
			else:
				self.image = self.images[2]
			if self.bottomleft_comp[0]>-400:
				self.bottomleft_comp[0]-=self.velocity
				return 2
			if self.bottomleft_comp[0]<=-400:
				# print('gfhjgh')
				self.rect.bottomleft = 1280,720
				self.bottomleft_comp = [1280,720]
				return 0
		# print(self.rect)


		

		# if self.rect.bottom< 521:
		# 	self.rect.move_ip(0,-1)
		# elif self.rect.bottom510:
		# 	self.rect.move_ip(0,1)

	def CheckOrder(self):
		pass

class realText(pygame.sprite.Sprite):
    def __init__(self,screen,pos,size) -> None:
        super().__init__()
        self.screen = screen
        self.pos = pos
        self.size = size
        self.original_size = self.size
        self.color=(250,250,250)
        self.myFont = pygame.font.Font("./assets/font/TanoheSans-Medium.ttf", self.size)
        self.image = self.myFont.render("_", 1, self.color)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        
    def update(self,message):
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.image = self.myFont.render(message, 1, self.color)

class OrderText(pygame.sprite.Sprite):
	def __init__(self,screen,pos,size,item_pos) -> None:
		super().__init__()
		self.item_pos=item_pos
		self.screen = screen
		self.pos = pos
		self.size = size
		self.original_size = self.size
		self.color=(200,200,200)
		self.myFont = pygame.font.Font("./assets/font/TanoheSans-Medium.ttf", self.size)
		self.image = self.myFont.render("_", 1, self.color)
		self.rect = self.image.get_rect()
		self.rect.center = self.pos
		self.item_images = [
			pygame.transform.scale(pygame.image.load("./assets/red_beans.png").convert_alpha(),(50,50)),
			pygame.transform.scale(pygame.image.load("./assets/sugar.png").convert_alpha(),(50,50)),
			pygame.transform.scale(pygame.image.load("./assets/water.png").convert_alpha(),(50,50)),
			pygame.transform.scale(pygame.image.load("./assets/heat.png").convert_alpha(),(50,50))
			]
		self.current_item_image = self.item_images[0]
		self.item_rect = self.current_item_image.get_rect()
		self.item_rect.center = self.item_pos
	def update(self,message,type):
		self.current_item_image = self.item_images[type]
		self.rect = self.image.get_rect()
		self.rect.center = self.pos
		self.image = self.myFont.render(message, 1, self.color)
		self.screen.blit(self.current_item_image,self.item_rect)

class JumpScare(pygame.sprite.Sprite):
	"""docstring for JumpScare"""
	def __init__(self,image_link,display):
		super().__init__()
		self.display = display

		self.bg = pygame.image.load("./assets/foods/Nothing.png").convert_alpha()
		self.image_link = image_link
		self.image = pygame.image.load(self.image_link).convert_alpha()
		self.original_image = self.image
		self.image = pygame.transform.scale(self.original_image, (0, 0))
		self.rect = self.image.get_rect()
		self.rect.center = (640,360)

		self.scalar = 0.1

		self.height =0
		self.width = 0


	def update(self,scare_now):
		if scare_now==True:
			self.display.blit(self.bg,(0,0,1280,720))
			# if is_alive==0:
			# 	self.kill()
			if self.height<=800:
				self.width+=1280*self.scalar
				self.height+=720*self.scalar
			# elif self.height>=800:
			# 	pass

			self.image = pygame.transform.scale(self.original_image, (int(self.width),int(self.height)))
			self.rect = self.image.get_rect(center = (640,360))
		# self.display.blit(self.image,self.rect)
	def kill_now(self):
		if self.height>=800:
			self.height =0
			self.width = 0
			return True

class MainGame(pygame.sprite.Sprite):
	"""docstring for MainGame"""
	def __init__(self, display):
		super().__init__()
		self.display = display
		#SOUND++++++++++++++++
		self.ANGER = pygame.mixer.Sound("./assets/music/sound/ANGER.ogg")
		self.OK_SOUND = pygame.mixer.Sound("./assets/music/sound/CLICK.ogg")

		self.current_hour = int(datetime.now().strftime("%H"))

		self.bg = pygame.image.load("./assets/bg.png").convert_alpha()
		self.bg = pygame.transform.scale(self.bg,(960,720))
		self.pot = pygame.image.load("./assets/pot.png").convert_alpha()
		self.pot = pygame.transform.scale(self.pot,(200,200))
		self.pot_rect = self.pot.get_rect()

		self.RedBeans = KitchenThings("./assets/red_beans.png",(150,150),self.display,'beans',200,200)
		self.Sugar = KitchenThings("./assets/sugar.png",(150,400),self.display,'sugar',200,200)
		self.Water = KitchenThings("./assets/water.png",(800,590),self.display,'water',325,195)
		self.Heat = KitchenThings("./assets/heat.png",(1150,650),self.display,'heat',213,114)
		self.CustomerTest = Customer(self.display)
		self.MyJump = JumpScare("./assets/scare.png",self.display)
		self.MyJump_group = pygame.sprite.Group()
		self.MyJump_group.add(self.MyJump)

		self.particle1 = ParticlePrinciple()
		self.PARTICLE_EVENT = pygame.USEREVENT + 1
		pygame.time.set_timer(self.PARTICLE_EVENT,40)

		#TEXT----------------------
		self.OrderText1 = OrderText(self.display, (530,100),40,(400,100))
		self.OrderText2 = OrderText(self.display, (530,170),40,(400,170))
		self.OrderText3 = OrderText(self.display, (530,240),40,(400,240))
		self.OrderText4 = OrderText(self.display, (530,330),40,(400,330))

		self.order_text_group1 = pygame.sprite.Group()
		self.order_text_group2 = pygame.sprite.Group()
		self.order_text_group3 = pygame.sprite.Group()
		self.order_text_group4 = pygame.sprite.Group()

		self.order_text_group1.add(self.OrderText1)
		self.order_text_group2.add(self.OrderText2)
		self.order_text_group3.add(self.OrderText3)
		self.order_text_group4.add(self.OrderText4)

		self.ScoreText = realText(self.display,(1070,50),30)
		self.ScoreText_group=pygame.sprite.Group()
		self.ScoreText_group.add(self.ScoreText)
		#------------------------

		#ORDER$$$$$$$$$$$$$$$
		self.my_order = [0,0,0,0]
		self.customer_order = [
			random.randint(0, 3),
			random.randint(0, 3),
			random.randint(0, 3),
			random.randint(0, 3)
		]

		self.customer_order_counting = [
		self.customer_order[0]-self.my_order[0],
		self.customer_order[1]-self.my_order[1],
		self.customer_order[2]-self.my_order[2],
		self.customer_order[3]-self.my_order[3],
		]
		#$$$$$$$$$$$$$$$$$

		#FADERS=======
		self.Red_Bean_Soup = "./assets/foods/Red_Bean_Soup.png"
		self.Beans_Cup = "./assets/foods/Beans_Cup.png"
		self.Sugar_Cup = "./assets/foods/Sugar_Cup.png"
		self.Sugar_Water = "./assets/foods/Sugar_Water.png"
		self.Water_Cup= "./assets/foods/Water_Cup.png"
		self.Nothing ="./assets/foods/Nothing.png"

		self.menu = [self.Red_Bean_Soup,self.Beans_Cup,self.Sugar_Cup,self.Sugar_Water,self.Water_Cup,self.Nothing]

		self.current_dish = order_image(self.customer_order)

		self.finished_dish1 = pygame.image.load(self.menu[self.current_dish]).convert_alpha()
		self.finished_dish1.set_alpha(0)
		self.alph = 0
		self.fading = False
		self.show_beans=False
		#============

		# calc_order_name(customer_order)
		#beans,sugar,water,heat

		self.order_correct = False
		self.side_bar_color = 'black'
		self.customer_status = 0
		self.SCORE = 0
		self.FAIL_COUNT=0
		self.can_jump = False
		self.do_boss = False
		self.mouse_pos = pygame.mouse.get_pos()
		self.mouse_press = pygame.mouse.get_pressed()[0]

		self.count_before_jumpscare = random.randint(1,3)

	def draw(self):
		# print('draw')
		if self.current_hour>=7 and self.current_hour<=11:
			self.display.fill((215,232,253))
			self.side_bar_color= (111,153,64)

		elif self.current_hour>=12 and self.current_hour<=17:
			self.display.fill((170,196,201))
			self.side_bar_color = (99,119,91)
		else:
			self.display.fill((48,64,90))
			self.side_bar_color=(115,112,0)

		self.display.blit(self.bg,(320,0))
		pygame.draw.rect(self.display, self.side_bar_color, pygame.Rect(0, 0, 320, 720))
		self.bean_counter = self.RedBeans.Draw(self.mouse_press,self.mouse_pos)
		self.sugar_counter = self.Sugar.Draw(self.mouse_press,self.mouse_pos)
		self.order_text_group1.update(str(self.customer_order_counting[0]),0)
		self.order_text_group2.update(str(self.customer_order_counting[1]),1)
		self.order_text_group3.update(str(self.customer_order_counting[2]),2)
		self.order_text_group4.update(str(self.customer_order_counting[3]),3)
		self.order_text_group1.draw(self.display)
		self.order_text_group2.draw(self.display)
		self.order_text_group3.draw(self.display)
		self.order_text_group4.draw(self.display)

		if self.do_boss == False:
			self.CustomerTest.Render()
			self.customer_status_output = self.CustomerTest.Move(self.customer_status,self.order_correct)
			self.customer_status = self.customer_status_output
			self.CustomerTest.Update()

		pygame.draw.rect(self.display, (170,135,54), pygame.Rect(0, 570, 1280, 150))

		self.water_counter = self.Water.Draw(self.mouse_press,self.mouse_pos)
		self.heat_counter = self.Heat.Draw(self.mouse_press,self.mouse_pos)
		self.display.blit(self.pot,(300,500))

		if self.do_boss==False:
			self.ScoreText_group.update('Happy Customers: '+str(self.SCORE))
			self.ScoreText_group.draw(self.display)

		self.finished_dish1.set_alpha(self.alph)
		self.display.blit(self.finished_dish1,(0,0))
		self.particle1.emit()

	def Initialize(self):
		# print('init')
		self.mouse_pos = pygame.mouse.get_pos()
		self.mouse_press = pygame.mouse.get_pressed()[0]

		self.customer_order_counting = [
		self.customer_order[0]-self.my_order[0],
		self.customer_order[1]-self.my_order[1],
		self.customer_order[2]-self.my_order[2],
		self.customer_order[3]-self.my_order[3],
		]
	def Update(self):
		# print('update')
		if self.bean_counter =='beans':
			self.my_order[0]+=1
		elif self.sugar_counter =='sugar':
			self.my_order[1]+=1
		elif self.water_counter =='water':
			self.my_order[2]+=1
		elif self.heat_counter =='heat':
			self.my_order[3]+=1
		if self.my_order == self.customer_order:
			self.current_dish = order_image(self.customer_order)
			self.finished_dish1 = pygame.image.load(self.menu[self.current_dish]).convert_alpha()

			pygame.mixer.Sound.play(self.OK_SOUND)
			self.order_correct=True
			self.customer_status = 2
			self.show_beans = True
			self.my_order = [0,0,0,0]
			self.SCORE +=1
			# print('score is '+str(self.SCORE))
			self.customer_order = [
				random.randint(0, 3),
				random.randint(0, 3),
				random.randint(0, 3),
				random.randint(0, 3)
			]
			print(self.customer_order)

		if sum(self.my_order) > sum(self.customer_order):
			pygame.mixer.Sound.play(self.ANGER)
			self.customer_status = 2
			self.order_correct=False
			self.my_order = [0,0,0,0]
			self.FAIL_COUNT+=1
			# print('reset order')

		if self.FAIL_COUNT>=self.count_before_jumpscare:
			self.count_before_jumpscare = random.randint(1, 3)
			self.can_jump=True
			self.FAIL_COUNT=0
			pygame.mixer.Sound.play(self.ANGER)
		print(self.count_before_jumpscare)
		# if self.SCORE>=3:
		# 	self.do_boss=True

		if self.can_jump==True:
			self.MyJump_group.update(self.can_jump)
			self.MyJump_group.draw(self.display)
			self.done_jump = self.MyJump.kill_now()
			if self.done_jump==True:
				self.can_jump=False

		if self.show_beans==True and self.fading==False:
			self.fading=False
			# print('coming')
			if self.alph <= 500:
				self.alph+=40
			if self.alph >=500:
				self.fading = True
				# print('false')
				self.show_beans=False
		if self.fading==True:
			# print('fading')
			self.alph-=40
			if self.alph<=0:
				self.fading =False

	def CheckInput(self):
		# print('check input')
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
			if event.type == self.PARTICLE_EVENT:
				self.particle1.add_particles()
	def ScoreReturn(self):
		# print(self.SCORE)
		return self.SCORE

class ScaleSprite(pygame.sprite.Sprite):
	def __init__(self, center, image_link,size):
		super().__init__()
		self.image_link = image_link		
		self.original_image = pygame.image.load(self.image_link).convert_alpha()
		self.image = self.original_image
		self.rect = self.image.get_rect(center = center)
		self.grow = 0
		self.speed = 100
		self.size=size
		self.size_x = self.size[0]
		self.size_y = self.size[1]
	def update(self):
		if self.grow > 1000:
			self.grow=1000
		self.grow += self.speed

		orig_x, orig_y = self.original_image.get_size()
		self.size_x = orig_x + round(self.grow)
		self.size_y = orig_y + round(self.grow)
		self.image = pygame.transform.scale(self.original_image, (self.size_x, self.size_y))
		self.rect = self.image.get_rect(center = self.rect.center)

class SlideShow(object):
	"""docstring for SlideShow"""
	def __init__(self,screen):
		super().__init__()
		self.screen = screen
		self.title_text = Text(self.screen,"Tasty Red Bean Simulator",(1280/2,720-720/5-720/20),100,False)
		# self.instruction_text = Text(self.screen,"press any button",(1280/2,720-720/15-720/30),50,True)
		self.text_group = pygame.sprite.Group()
		self.text_group.add(self.title_text)
		# self.text_group.add(self.instruction_text)
		self.images = [
		pygame.image.load("./assets/title/title1.png").convert_alpha(),
		pygame.image.load("./assets/title/nasa_mars.jpeg").convert_alpha(),
		pygame.image.load("./assets/title/title2.png").convert_alpha(),
		pygame.image.load("./assets/title/title5.png").convert_alpha(),
		pygame.image.load("./assets/title/nasa_rover.jpeg").convert_alpha(),
		pygame.image.load("./assets/title/title3a.png").convert_alpha(),
		pygame.image.load("./assets/title/title4.png").convert_alpha(),
		]
		self.index = 0
		self.image = self.images[self.index]
		self.rect=self.image.get_rect()
		self.alph = 10
		self.image.set_alpha(self.alph)
		self.mode = 1
	def draw(self):
		self.screen.fill('black')
		if self.alph >=400:
			self.mode =-1
		elif self.alph <=-0:
			self.index+=1
			if self.index>len(self.images)-1:
				self.index=0
			self.image = self.images[self.index]
			self.mode=1

		self.alph +=10*self.mode
		self.image.set_alpha(self.alph)


		self.screen.blit(self.image,self.rect)

		self.text_group.update(True)
		self.text_group.draw(self.screen)


		


class Title(object):
	"""docstring for TitleImage"""
	def __init__(self, size,screen):
		super().__init__()
		self.size = size
		self.screen = screen

		self.Title1 = JumpScare("./assets/title/title1.png",self.screen)
		self.Title2 = JumpScare("./assets/title/title2.png",self.screen)
		self.Title3 = JumpScare("./assets/title/title3.png",self.screen)
		self.Title4 = JumpScare("./assets/title/title4.png",self.screen)
		self.Title5 = JumpScare("./assets/title/title5.png",self.screen)
		self.mouse_pos = pygame.mouse.get_pos()
		self.mouse_press = pygame.mouse.get_pressed()[0]

	def Draw(self):
		print('draw')
		self.Title1.update(True)


MySlides = SlideShow(screen)
title_done = False
particle1=ParticlePrinciple()
PARTICLE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(PARTICLE_EVENT,100)
while not title_done:
	for event in pygame.event.get():
		if event.type == PARTICLE_EVENT:
			particle1.add_particles()
		if event.type == pygame.QUIT:
			quit()
		if event.type == pygame.KEYDOWN:
			print('poo')
			title_done = True
	if pygame.mouse.get_pressed()[0] == True:
		title_done=True
	MySlides.draw()
	particle1.emit()
	clock.tick(30)
	pygame.display.flip()


done = False
MyGame = MainGame(screen)
while not done:
	clock.tick(30)

	myscore = MyGame.ScoreReturn()

	MyGame.CheckInput()
	MyGame.Initialize()
	MyGame.draw()
	MyGame.Update()
	if myscore>=3:
		print(myscore)
		done=True
	pygame.display.flip()



	
