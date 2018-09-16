#
# A simple typing game that forces you to write the letters in reverse order
# This enforces active engagement thats very important in learning new skills
#

import pygame
import sys
import string
import random

#colors
blue=(0,128,255)
black=(0,0,0)
white=(255,255,255)
red=(255,0,0)

#costant variables
width =800
height=600


pygame.init()
pygame.font.init()
font=pygame.font.SysFont('monospace', 30)
screen=pygame.display.set_mode((width, height))
pygame.display.set_caption("reverser")
clock=pygame.time.Clock()

def generate_word(length):
    word=""
    for x in range(length):
        word+=random.choice(string.ascii_letters+string.digits)
    return word

speed=15
lives=3
level=1
score=0
done=False
word=generate_word(level+4)

x_pos=0
y_pos=0

class word():
    #This class represents a word and all its functions
    def __init__(self):
        self.word=generate_word(level+4)
        self.x= randint(0, width-10)
        self.y= 0

def update_y_pos(y_pos):
    if(y_pos<height):
        y_pos+=4
    else:
        y_pos=0
    return y_pos


while not done:
    if y_pos>=height:
        word=generate_word(level+4)
        lives-=1
    if lives==0:
        pygame.quit()
        sys.exit()
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
    text=font.render(word, True, (0,128,0))
    w=text.get_rect().width
    h=text.get_rect().height
    screen.blit(text,(0.5*(width-w), y_pos))
    
    pygame.display.flip()
    clock.tick(speed)

    #Update those variables for the next cycle
    y_pos=update_y_pos(y_pos)

