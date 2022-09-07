import pygame
pygame.mixer.pre_init()
pygame.init()
# pygame.mouse.set_visible(False)

screen = pygame.display.set_mode((1280, 720))
draft = pygame.image.load("./assets/draft.png").convert_alpha()

pot = pygame.image.load("./assets/pot.png").convert_alpha()
pot = pygame.transform.scale(pot,(200,200))
pot_rect = pot.get_rect()


redbeans = pygame.image.load("./assets/red_beans.png").convert_alpha()
redbeans = pygame.transform.scale(redbeans,(200,200))
redbeans_rect = redbeans.get_rect()

sugar = pygame.image.load("./assets/sugar.png").convert_alpha()
sugar = pygame.transform.scale(sugar,(200,200))
sugar_rect = sugar.get_rect()

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
		self.kind = kind

		self.can_activate = True


	def Draw(self,active,mouse_pos):
		
		if active==True and self.rect.collidepoint(mouse_pos):
			self.display.blit(self.image_big,self.rect)
			if self.can_activate==True:
				self.can_activate = False
				print(self.kind)
				
		else:
			self.can_activate=True
			self.display.blit(self.image,self.rect)





RedBeans = KitchenThings("./assets/red_beans.png",(150,150),screen,'beans',200,200)
Sugar = KitchenThings("./assets/sugar.png",(150,400),screen,'sugar',200,200)
Water = KitchenThings("./assets/water.png",(820,590),screen,'water',325,195)

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quit()

	mouse_pos = pygame.mouse.get_pos()
	mouse_press = pygame.mouse.get_pressed()[0]



	screen.blit(draft,(0,0))
	screen.blit(pot,(300,500))
	RedBeans.Draw(mouse_press,mouse_pos)
	Sugar.Draw(mouse_press,mouse_pos)
	Water.Draw(mouse_press,mouse_pos)

	screen.blit(customer,(570,20))



	pygame.display.flip()