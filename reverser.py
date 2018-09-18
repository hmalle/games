#
# A simple typing game that forces you to write the letters in reverse order
# This enforces active engagement thats very important in learning new skills
#

import pygame, sys, string, random

#Colors
blue =(0,128,255)
black=(0,0,0)
white=(255,255,255)
red  =(255,0,0)
green=(255,0,0)
color1=(56,104,106)

#Variables
width =800
height=600

#Pygame initializations
pygame.init()
pygame.font.init()
font=pygame.font.SysFont('monospace', 20)
screen=pygame.display.set_mode((width, height))
pygame.display.set_caption("reverser")
clock=pygame.time.Clock()

class Word(pygame.sprite.Sprite):
    def __init__(self, level):
        pygame.sprite.Sprite.__init__(self)
        self.x=0
        self.y=0
        self.text=self.generate_random_word(level)

    def is_past_height(self):
        if(self.y>height):
            return True
        else: 
            return False

    def update_position(self):
        self.y+=5 

    def generate_random_word(self,level):
        return "".join(random.choice(string.letters+string.digits)for x in range(level+4))

class Player():
    level=1
    
def main():
    #The game loop
    done=False
    player = Player()
    word=Word(player.level)

    while not done:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
        #Generate random words that drops on the screen
        screen.fill(black)
        text=font.render(word.text, True, white)
        screen.blit(text,(word.x,word.y))
        pygame.display.update()
        word.update_position()
        clock.tick(30)      #Frames per second

if __name__ == '__main__':
    main()

