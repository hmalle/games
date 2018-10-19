
"""
A simple typing game that forces you to write the letters in reverse order
This enforces active engagement thats very important in learning new skills
"""

import pygame, sys
from math import log
import time
import random, string

class Word:
    def __init__(self, level, width, height):
        self.level= level
        self.text=self.generate()
        self.x=0
        self.y=0
        self.screen_w=width
        self.screen_h=height
        self.level=level

    def generate(self):
        length=5+int(log(self.level))
        text=""
        for _ in range(length):
            text+=random.choice(string.letters+string.digits)
        print('word generated '+text)
        return text
        
class Player:
    def __init__(self, screen_w, screen_h):
        self.screen_w = screen_w
        self.screen_h = screen_h
        self.words=[]
        self.level=1
        self.interval=5 #5 seconds between words generation
        self.last_time=time.time()

    def update(self):
        time_now = time.time()
        if time_now-self.last_time >= self.interval:
            self.last_time=time_now
            self.add_new_word()


    def add_new_word(self):
        self.words.append(Word(self.level,self.screen_w, self.screen_h))

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
    
    #Our character
    player = Player(width,height)

    while(True):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.font.quit()
                pygame.quit()
                sys.exit()

        player.update()

        clock.tick(fps)

    pygame.quit()

if __name__=='__main__': main()
