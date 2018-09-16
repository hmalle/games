#
# A simple typing game that forces you to write the letters in reverse order
# This enforces active engagement thats very important in learning new skills
#

import pygame, sys, string, random

class Word():
    def __init__(self):
        self.text=generate_word(level+4)
        self.x= randint(0, width-10)
        self.y= 0   #Only the y will change
        self.speed=2
        self.level=1
    def update_position(self):
        self.y = self.y + self.speed

class Player():
    def __init__(self):
        self.lives=3
        self.level=1

def main():
    #Define colors
    blue =(0,128,255)
    black=(0,0,0)
    white=(255,255,255)
    red  =(255,0,0)
    #costant variables
    width =800
    height=600
    speed=15
    lives=3
    level=1
    score=0
    done=False

    x_pos=0
    y_pos=0


    #Pygame initializations
    pygame.init()
    pygame.font.init()
    font=pygame.font.SysFont('monospace', 30)
    screen=pygame.display.set_mode((width, height))
    pygame.display.set_caption("reverser")
    clock=pygame.time.Clock()

if __name__ == '__main__':
    main()

