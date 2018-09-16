#
# A simple typing game that forces you to write the letters in reverse order
# This enforces active engagement thats very important in learning new skills
#

import pygame
import sys
import string
import random

pygame.init()
pygame.font.init()

font=pygame.font.SysFont('monospace', 30)

#colors
blue=(0,128,255)
black=(0,0,0)
white=(255,255,255)

#costant variables
width =600
height=400

screen=pygame.display.set_mode((width, height))
pygame.display.set_caption("reverser")
clock=pygame.time.Clock()
done=False

x_pos=0
y_pos=0

def update_y_pos(y_pos):
    if(y_pos<height):
        y_pos+=4
    else:
        y_pos=0
    return y_pos

def generate_word(length):
    word=""
    for x in range(length):
        word+=random.choice(string.ascii_letter+string.digits)
    return word

while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN and event.key==pygame.K_RETURN:
            pass
            
    #Erase the screen
    screen.fill(black)
    #my_rect=pygame.draw.rect(screen, blue, pygame.Rect(x_pos, y_pos, width, 30))

    #Fonts testing
    text=font.render("Hellow World", True, (0,128,0))
    w=text.get_rect().width
    h=text.get_rect().height
    screen.blit(text,(0.5*(width-w), y_pos))
    
    pygame.display.flip()
    clock.tick(30)

    #Update those variables for the next cycle
    y_pos=update_y_pos(y_pos)

