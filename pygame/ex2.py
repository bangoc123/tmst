import pygame

BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)

pygame.init()
size = (700, 900)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Load Image")

done = False

clock = pygame.time.Clock()

carImg = pygame.image.load('car12.png')
angle = 0
def placeCar(x,y):
	screen.blit(carImg, (x,y))

def rotateCar(x, y, angle):
	rotatedCar = pygame.transform.rotate(carImg, angle)
	screen.blit(rotatedCar, (x, y))


while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

	screen.fill(WHITE)
	#placeCar(100,200)
	
	angle +=2
	if angle>360:
		angle = 0
	rotateCar(100, 200, angle)
	pygame.display.flip()		
	clock.tick(60)