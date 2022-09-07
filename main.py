import pygame
pygame.mixer.pre_init()
pygame.init()
screen = pygame.display.set_mode((1280, 720))
draft = pygame.image.load("./assets/draft.png").convert_alpha()


class Ingredients(pygame.sprite.Sprite):
	"""docstring for ClassName"""
	def __init__(self, image_link, coords, display):
		super().__init__()
		self.image_link = image_link
		self.image = pygame.image.load(self.image_link).convert_alpha()
		self.rect = self.image.get_rect()
		self.display = display
		self.coords = coords
	def Render(self):
		self.display.blit(pygame.transform.scale(self.image,(200,200)),(self.coords[0],self.coords[1]))

class Pot(pygame.sprite.Sprite):
	"""subclass of ingredients?"""
	def __init__(self, coords, display):
		super().__init__()
		self.display = display
		self.image = pygame.image.load('./assets/pot.png').convert_alpha()
		self.image = pygame.transform.scale(self.image, (200, 200))
		self.rect =self.image.get_rect()
		self.move_object = False
		self.coord_store = (400,630)
		self.click_activate_count =0

	def Render(self,coords):

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
			if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(coords) ==True:
				self.click_activate_count +=1

				if self.click_activate_count ==2:
					self.click_activate_count=0
					self.coord_store = coords
					self.move_object = False

			elif event.type == pygame.MOUSEBUTTONUP and self.click_activate_count==1:
				self.move_object = True

		if self.move_object == True:
			self.rect.x = coords[0]-100
			self.rect.y = coords[1]-100
		else:
			self.rect.x = self.coord_store[0]-100
			self.rect.y = self.coord_store[1]-100

		self.display.blit(self.image,self.rect)



class Customer(pygame.sprite.Sprite):
	"""docstring for ClassName"""
	def __init__(self, display):
		super().__init__()
		self.display = display
		self.image = pygame.image.load('./assets/customer_test.png').convert_alpha()
		self.rect = self.image.get_rect()
	def Render(self):
		self.display.blit(pygame.transform.scale(self.image,(200,200)),(100,100))
	def CheckOrder(self):
		pass


done = False

RedBeans = Ingredients('./assets/red_beans.png',(0,0),screen)
MyPot = Pot((0,0),screen)
Customers = Customer(screen)

while not done:

	mouse_pos = pygame.mouse.get_pos()
	# print(mouse_pos)
	screen.blit(draft,(0,0))
	MyPot.Render(mouse_pos)


	# pygame.draw.rect(screen, 'red', (mouse_pos[0]-50,mouse_pos[1]-50, 100, 100))
	pygame.display.flip()