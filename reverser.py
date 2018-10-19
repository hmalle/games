
"""
A simple typing game that forces you to write the letters in reverse order
This enforces active engagement thats very important in learning new skills
"""

import pygame, sys
from math import log
import random, string

class Word:
    def __init__(self, level, width,height):
        self.level= level
        self.text=generate(self.level)
        self.x=0
        self.y=0
        self.text_h=0 
        self.text_h=0
        self.screen_w=width
        self.screen_h=height
        self.level=level

class Player:
    def __init__(self, screen_w, screen_h):
        self.screen_w = screen_w
        self.screen_h = screen_h
        self.words_list=[]
        self.level=1

    def add_new_word(self):
        self.wordlist.append(Word(self.level,screen_w, screen_h))

def main():
    #data
    fps=20
    width,height=800,600
    #Initializations
    pygame.init()
    pygame.font.init()
    screen=pygame.display.set_mode((width,height))
    font=pygame.font.SysFont('monospace',30)
    pygame.display.set_caption("revereserever")
    clock=pygame.time.Clock()

    while(True):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.font.quit()
                pygame.quit()
                sys.exit()
    
    pygame.quit()

if __name__=='__main__': main()
