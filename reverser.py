#
# A simple typing game that forces you to write the letters in reverse order
# This enforces active engagement thats very important in learning new skills
#

import pygame, sys, string, random, time

#Colors
blue =(0,128,255)
black=(0,0,0)
white=(255,255,255)
red  =(255,0,0)
green=(255,0,0)
color1=(56,104,106)
orange=(255,165,0)
tomato_red=(255,60,0)

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

class Word():
    def __init__(self, level):
        self.x=random.randint(0,width-10) #TODO: Minus word length box
        self.y=0
        self.text=self.generate_random_word(level)
        self.color=self.get_color()

    def get_color(self):
        if self.y>(height-100):
            return red
        elif self.y>(height-200):
            return orange
        else:
            return white

    def is_past_height(self):
        if(self.y>height):
            return True
        else: 
            return False

    def update_word(self):
        self.y+=2  #Move the word 1 pixel down
        self.color=self.get_color()

    def generate_random_word(self, char_count):
        random_word="".join(random.choice(string.letters+string.digits)for x in range(char_count))
        return random_word.lower()
    
def main():
    #The game loop
    done=False
    char_count=5
    wordlist=[]
    wordlist.append(Word(char_count))
    time_interval=4
    correct=0
    missed_words=0
    user_word=""
    start=time.time()
    while not done:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            #When the enter key is pressed, check the word thats been entered
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:
                    print(user_word)
                    for word in wordlist:
                        if word.text==user_word:
                            wordlist.remove(word)
                            correct+=1
                    user_word=""
                #Check the lower case asciis and the digits only
                elif (event.key>=97 and event.key<=122) or (event.key>=48 and event.key<=57):
                    user_word+=str(unichr(event.key))
                else:
                    pass

        screen.fill(black)
        #Generate a new word after every few seconds
        now=time.time();
        if now-start>=time_interval:
            start=time.time()
            wordlist.append(Word(char_count))

        #Render words on the screen and delete those not completeled
        for word in wordlist:
            if word.y > height:
                wordlist.remove(word)
                missed_words+=1
            else:
                text=font.render(word.text, True, word.color)
                screen.blit(text,(word.x,word.y))
                word.update_word()  #Update here to avoid having anther loop

        pygame.display.update()

        clock.tick(20) #Frames per second

if __name__ == '__main__':
    main()

