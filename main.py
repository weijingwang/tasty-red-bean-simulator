import pygame
pygame.mixer.pre_init()
pygame.init()
# pygame.mouse.set_visible(False)

screen = pygame.display.set_mode((1280, 720))
draft = pygame.image.load("./assets/draft.png").convert_alpha()

pot = pygame.image.load("./assets/pot.png").convert_alpha()
pot = pygame.transform.scale(pot,(200,200))
pot_rect = pot.get_rect()

customer = pygame.image.load("./assets/customer_test.png").convert_alpha()
customer = pygame.transform.scale(customer,(500,500))
customer_rect = customer.get_rect()

done = False




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


	def Draw(self,active,mouse_pos):
		
		if active==True and self.rect.collidepoint(mouse_pos):
			self.display.blit(self.image_big,self.rect)
			if self.can_activate==True:
				# if self.rect.colliderect(pygame.Rect(200,200,350,550))==False:
				# 	print
				# 	self.rect.move_ip((350-self.rect.center[0])/4, (550-self.rect.center[1])/4)
				# else:
				self.can_activate = False

				# print(self.kind)
				# print(self.rect.center)
				return self.kind

				
		else:
			self.can_activate=True
			self.display.blit(self.image,self.rect)





RedBeans = KitchenThings("./assets/red_beans.png",(150,150),screen,'beans',200,200)
Sugar = KitchenThings("./assets/sugar.png",(150,400),screen,'sugar',200,200)
Water = KitchenThings("./assets/water.png",(820,590),screen,'water',325,195)
Heat = KitchenThings("./assets/heat.png",(1170,600),screen,'heat',213,114)


order = [0,0,0,0]
#beans,sugar,water,heat

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quit()

	mouse_pos = pygame.mouse.get_pos()
	mouse_press = pygame.mouse.get_pressed()[0]



	screen.blit(draft,(0,0))
	screen.blit(pot,(300,500))
	bean_counter = RedBeans.Draw(mouse_press,mouse_pos)
	sugar_counter = Sugar.Draw(mouse_press,mouse_pos)
	water_counter = Water.Draw(mouse_press,mouse_pos)
	heat_counter = Heat.Draw(mouse_press,mouse_pos)

	if bean_counter =='beans':
		order[0]+=1
	elif sugar_counter =='sugar':
		order[1]+=1
	elif water_counter =='water':
		order[2]+=1
	elif heat_counter =='heat':
		order[3]+=1

	print(order)
	screen.blit(customer,(570,20))



	pygame.display.flip()