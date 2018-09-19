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

def check_answer(wordlist[], user_word):
    for word in wordlist:
        if user_word==word:
           wordlist.remove(word) 

class Word(pygame.sprite.Sprite):
    def __init__(self, level):
        pygame.sprite.Sprite.__init__(self)
        self.x=random.randint(0,width)
        self.y=0
        self.text=self.generate_random_word(level)

    def is_past_height(self):
        if(self.y>height):
            return True
        else: 
            return False

    def update_position(self):
        self.y+=5 

    def generate_random_word(self, char_count):
        return "".join(random.choice(string.letters+string.digits)for x in range(char_count))
    
def main():
    #The game loop
    done=False
    player = Player()
    char_count=5
    word=Word(char_count)
    wordlist=[]
    user_word=""
    while not done:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_ENTER:
                    check_answer(user_word, wordlist)
 
        #Generate random words that drops on the screen
        screen.fill(black)
        for word in wordlist:
            
        text=font.render(word.text, True, white)
        screen.blit(text,(word.x,word.y))
        pygame.display.update()
        word.update_position()
        clock.tick(20)      #Frames per second

if __name__ == '__main__':
    main()

