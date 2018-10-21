
"""
A simple typing game that forces you to write the letters in reverse order
This enforces active engagement thats very important in learning new skills
"""

import pygame, sys
from math import log
import time
from random import choice, randint
from string import letters, digits

#Colors
ucolor = "#e0fbfc"    # color for the upper part of screen
mcolor = "#eac435"   #color for middle part of screen
lcolor = "#e94f37"    #color for the lower part of the screen
bgcolor= "#0b0500"  #background color

def rgb(hexcolor):
    hexcolor = hexcolor.lstrip('#')
    return tuple(int(hexcolor[i:i+2],16) for i in (0,2,4))

class Word:
    def __init__(self, level, width, height, font):
        self.x=0
        self.y=0
        self.text_color = ucolor
        self.width=0
        self.height=0
        self.screen_w=width
        self.screen_h=height
        self.level=level
        self.font=font
        self.word=""  #To be set by generate
        self.text=self.generate()
        
    def generate(self):
        length=5+int(log(self.level))
        word=""
        for _ in range(length):
            word+=choice(letters+digits)
        self.word = word
        text = self.font.render(word,True, rgb(self.text_color))
        self.width=text.get_width()
        self.height=text.get_height()
        self.x = randint(0, self.screen_w-self.width)
        self.y= 0
        return text
    
    def update_color(self):
        if self.y < 0.6*self.screen_h:
            self.text_color = ucolor
        elif self.y<0.8*self.screen_h:
            self.text_color = mcolor
        else:
            self.text_color = lcolor
        #update color of the text to be rendered
        self.text=self.font.render(self.word,True, rgb(self.text_color))
        
class Player:
    def __init__(self, screen, screen_w, screen_h):
        self.screen_w = screen_w
        self.screen_h = screen_h
        self.words=[]
        self.level=1
        self.font=pygame.font.SysFont("monospace", 25)
        self.screen=screen
        self.interval=5 #3 seconds between words generation
        self.last_time=time.time()-5 #Initially -5 so self.update generates first word right away

    def update(self):
        #Update the position for each word and its corresponding color
        for word in self.words:
            #word.x+=5 #Later on change the x position so make the letters move across the screen
            word.y+=5
            word.update_color()
        #Delete words past the screen length
        for word in self.words:
            if word.y > self.screen_h:
                self.words.remove(word)
        #Check time and create a new word
        time_now = time.time()
        if time_now-self.last_time >= self.interval:
            self.last_time=time_now
            self.add_new_word()
        #Place words on the screen
        for word in self.words:
            #w=font.render(word.text,True,(255,0,0))
            #screen.blit(w, (word.x, word,y)
            self.screen.blit(word.text,(word.x, word.y))

    def add_new_word(self):
        self.words.append(Word(self.level,self.screen_w, self.screen_h,self.font))

def main():
    #data
    fps=20
    width,height=700,900
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
        screen.fill(rgb(bgcolor))
        player.update()
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()

if __name__=='__main__': main()
