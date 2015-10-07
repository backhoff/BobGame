import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Testing Pygame')
clock = pygame.time.Clock()

bobImg = pygame.image.load('bob.png')
bobWidth = 32
thing_width = 60
thing_height = 60
thisColor = white


def speed(speed):
	font = pygame.font.SysFont(None, 25)
	text = font.render("Speed: " + str(speed), True, white)
	gameDisplay.blit(text,(700,0))


def score(dodgedCount):
	font = pygame.font.SysFont(None, 25)
	text = font.render("Score: " + str(dodgedCount), True, white)
	gameDisplay.blit(text,(0,0))

def message_displayCenter(textToDisplay,size,x,y):
	largeText = pygame.font.Font('freesansbold.ttf', size)
	TextSurf, TextRect = text_objects(textToDisplay, largeText)
	TextRect.center = (x,y)
	gameDisplay.blit(TextSurf,TextRect)

	pygame.display.update()

	time.sleep(2)


	game_loop()

def things(thingx, thingy, thingw, thingh):
	pygame.draw.rect(gameDisplay, (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255)),[thingx,thingy,thingw, thingh])

def text_objects(text, font):
	textSurface = font.render(text, True, white)
	return textSurface, textSurface.get_rect()

def lost():
	message_displayCenter('You lost!',80,(display_width/2),(display_height/2))
	

def drawBob(x,y):
	gameDisplay.blit(bobImg,(x,y))

def game_loop():
	x = (display_width * 0.45)
	y = (display_height * 0.8)
	xChanged = 0

	thing_startx = random.randrange((0+thing_width),(display_width-thing_width))
	thing_starty = -600
	thing_speed = 10
	dodged = 0

	gameExit = False

	while not gameExit:
		# Crashing Loop
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key ==	 pygame.K_ESCAPE:
					pygame.quit()
					quit()


		#Movement on X (32-41)
			if event.type == pygame.KEYDOWN:
				if event.key ==	 pygame.K_LEFT:
						xChanged = -5
				elif event.key == pygame.K_RIGHT:
						xChanged = 5

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					xChanged = 0

		
		x += xChanged
		gameDisplay.fill(black)
		things(thing_startx, thing_starty, thing_width, thing_height)
		thing_starty += thing_speed
		drawBob(x, y)
		score(dodged)
		speed(thing_speed)

		if x > display_width+5 - bobWidth or x < -5:	
			message_displayCenter('You went off screen!',40,(display_width/2),(display_height/2))

		if thing_starty > display_height:
			dodged += 1
			thing_starty = 0 - thing_height
			thing_startx = random.randrange(0,display_width)
			if thing_speed < 20:
				thing_speed += 1       

		if y < thing_starty + thing_height:
			if x > thing_startx and x < thing_startx + thing_width or x + bobWidth > thing_startx and x + bobWidth < thing_startx + thing_width:
				lost()


		
		print(thing_speed)
		pygame.display.update()
		clock.tick(60)

game_loop()
pygame.quit()
quit()