import pygame
pygame.mixer.pre_init()
pygame.init()
# pygame.mouse.set_visible(False)

screen = pygame.display.set_mode((1280, 720))
draft = pygame.image.load("./assets/draft.png").convert_alpha()


class KitchenThings(pygame.sprite.Sprite):
	def __init__(self,image_link,coord_store, display,kind):
		super().__init__()
		self.image_link=image_link
		self.display = display
		self.image = pygame.image.load(self.image_link).convert_alpha()
		self.image = pygame.transform.scale(self.image, (200, 200))
		self.rect =self.image.get_rect()
		self.move_object = False
		self.coord_store = coord_store
		self.click_activate_count =0
		self.kind = kind
		self.using_rn = False
		# if self.kind ==



	def Render(self,coords):
		if pygame.mouse.get_pressed()[0] ==True and self.rect.collidepoint(coords) ==True:
			self.using_rn = True
			self.click_activate_count=True
			self.rect.x = coords[0]-100
			self.rect.y = coords[1]-100
			self.coord_store = coords
		else:
			self.using_rn = False
			self.click_activate_count=False
			self.rect.x = self.coord_store[0]-100
			self.rect.y = self.coord_store[1]-100
		self.display.blit(self.image,self.rect)

	def check_use(self):
		return self.using_rn


class Customer(pygame.sprite.Sprite):
	"""docstring for ClassName"""
	def __init__(self, display):
		super().__init__()
		self.display = display
		self.image = pygame.image.load('./assets/customer_test.png').convert_alpha()
		self.rect = self.image.get_rect()
	def Render(self):
		self.display.blit(pygame.transform.scale(self.image,(500,500)),(570,20))
	def CheckOrder(self):
		pass





done = False

MyPot = KitchenThings('./assets/pot.png',(400,630),screen,'pot')
RedBeans=KitchenThings('./assets/red_beans.png',(150,150),screen,'ingredient')
Sugar=KitchenThings('./assets/sugar.png',(150,400),screen,'ingredient')

Customers = Customer(screen)

# cursor = pygame.image.load("./assets/cursor.png").convert_alpha()
# cursor_closed = pygame.image.load("./assets/cursor_closed.png").convert_alpha()

# cursor_rect = cursor.get_rect()
# click_activate_count = 0

currently_dragging = False



while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quit()

	mouse_pos = pygame.mouse.get_pos()
	# print(mouse_pos)


	screen.blit(draft,(0,0))
	Customers.Render()
	MyPot.Render(mouse_pos)
	RedBeans.Render(mouse_pos)
	Sugar.Render(mouse_pos)
	

	if RedBeans.check_use() ==True:
		pass

	# cursor_rect.center = pygame.mouse.get_pos()
	# if pygame.mouse.get_pressed()[0] == False and click_activate_count==0:
	# 	screen.blit(cursor, cursor_rect)
	# elif pygame.mouse.get_pressed()[0] == True:
	# 	click_activate_count += 1
	# elif click_activate_count >0:
	# 	screen.blit(cursor_closed, cursor_rect)
	# elif click_activate_count ==2:
	# 	click_activate_count=0

	# pygame.draw.rect(screen, 'red', (mouse_pos[0]-50,mouse_pos[1]-50, 100, 100))
	pygame.display.flip()