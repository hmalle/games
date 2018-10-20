
"""
A simple typing game that forces you to write the letters in reverse order
This enforces active engagement thats very important in learning new skills
"""

import pygame, sys
from math import log
import time
import random
from string import letters, digits

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
            text+=random.choice(letters+digits)
        self.x
        return text
        
class Player:
    def __init__(self, screen, screen_w, screen_h):
        self.screen_w = screen_w
        self.screen_h = screen_h
        self.words=[]
        self.level=1
        self.font=pygame.font.SysFont("monospace", 25)
        self.screen=screen
        self.interval=5 #5 seconds between words generation
        self.last_time=time.time()-5 #Initially -5 so self.update generates first word right away

    def update(self):
        #Update the position for each word
        for word in self.words:
            #word.x+=5 #Later on change the x position so make the letters move across the screen
            word.y+=5
        #Delete words past the screen length
        for word in self.words:
            if word.y > self.screen_h:
                self.words.remove(word)
        """
        for index in range(len(self.words)):
            try:
                if self.words[index].y > self.screen_h:
                    self.words.pop(index)
            except:
                pass
                print("Index ",index," words length ",len(self.words))
        """
        #Check time and create a new word
        time_now = time.time()
        if time_now-self.last_time >= self.interval:
            self.last_time=time_now
            self.add_new_word()
        #Place words on the screen
        for word in self.words:
            #w=font.render(word.text,True,(255,0,0))
            #screen.blit(w, (word.x, word,y)
            self.screen.blit(self.font.render(word.text,True,(255,0,0)), (word.x, word.y))

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
    font=pygame.font.SysFont("monospace",30)
    pygame.display.set_caption("revereserever")
    clock=pygame.time.Clock()
    
    #Our character
    player = Player(screen,width,height)

    while(True):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.font.quit()
                pygame.quit()
                sys.exit()
        screen.fill((0,0,0))
        player.update()
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()

if __name__=='__main__': main()
