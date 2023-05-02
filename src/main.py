import pygame

def start():
	pygame.init()
	screen=pygame.display.set_mode((640,480))
	
	screen.fill((0,0,0))
	pygame.display.flip()

start()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
