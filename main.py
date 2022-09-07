import pygame
pygame.mixer.pre_init()
pygame.init()
screen = pygame.display.set_mode((1280, 720))
draft = pygame.image.load("./assets/draft.png").convert_alpha()


class Ingredients():
	"""docstring for ClassName"""
	def __init__(self, image_link, coords, display):
		self.image_link = image_link
		self.image = pygame.image.load(self.image_link).convert_alpha()
		self.rect = self.image.get_rect()
		self.display = display
		self.coords = coords
	def Render(self):
		self.display.blit(pygame.transform.scale(self.image,(200,200)),(self.coords[0],self.coords[1]))

class Pot():
	"""subclass of ingredients?"""
	def __init__(self, coords, display):
		self.display = display
		self.image = pygame.image.load('./assets/pot.png').convert_alpha()
		self.image = pygame.transform.scale(self.image, (200, 200))
		self.rect =self.image.get_rect()

	def Render(self,coords):

		self.rect = (coords[0]-100,coords[1]-100)
		# if x<=315:
		# 	x = 315
		# elif x >= 1280:
		# 	x = 1280
		# elif y <= 0+200:
		# 	y = 0
		# elif y >= 720:
		# 	y = 720


		self.display.blit(self.image,self.rect)



class Customer():
	"""docstring for ClassName"""
	def __init__(self, display):
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

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quit()
	mouse_pos = pygame.mouse.get_pos()
	print(mouse_pos)
	screen.blit(draft,(0,0))
	MyPot.Render(mouse_pos)


	# pygame.draw.rect(screen, 'red', (mouse_pos[0]-50,mouse_pos[1]-50, 100, 100))
	pygame.display.flip()