import pygame
pygame.mixer.pre_init()
pygame.init()
screen = pygame.display.set_mode((1280, 720))
draft = pygame.image.load("./assets/draft.png").convert_alpha()



class Ingredients():
	"""docstring for ClassName"""
	def __init__(self, arg):
		self.arg = arg


class Pot():
	"""subclass of ingredients"""
	def __init__(self, arg):
		self.arg = arg


class Customer():
	"""docstring for ClassName"""
	def __init__(self, arg):
		self.arg = arg






done = False
while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quit()
	mouse_pos = pygame.mouse.get_pos()

	screen.blit(draft,(0,0))
	pygame.draw.rect(screen, 'red', (mouse_pos[0]-50,mouse_pos[1]-50, 100, 100))
	pygame.display.flip()