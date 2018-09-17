#
# A simple typing game that forces you to write the letters in reverse order
# This enforces active engagement thats very important in learning new skills
#

import pygame, sys, string, random
from pygame.locals import *

#Colors
blue =(0,128,255)
black=(0,0,0)
white=(255,255,255)
red  =(255,0,0)

#Variables
width =800
height=600

#Pygame initializations
pygame.init()
pygame.font.init()
font=pygame.font.SysFont('monospace', 30)
screen=pygame.display.set_mode((width, height))
pygame.display.set_caption("reverser")
clock=pygame.time.Clock()



class Word(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.text=''.join(random.choice(string.ascii_letters)for x in range(5))
        self.x= randint(0, width-10)
        self.y= 0   #Only the y will change
        self.speed=2
        self.level=1
        
    def update_position(self):
        self.y = self.y + self.speed

def main():
    speed=15
    lives=3
    level=1
    score=0
    done=False

    while not done:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        #Generate random words that drops on the screen
        pygame.display.update()


if __name__ == '__main__':
    main()

