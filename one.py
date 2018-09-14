
import pygame
pygame.init()

#colors
blue=(0,128,255)

#costant variables
width =600
height=400


screen=pygame.display.set_mode((width, height))
done=False

while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True;
        screen.fill(blue)
        pygame.draw.rect(screen, blue, pygame.Rect(30, 30, 60, 60))
        pygame.display.flip()
