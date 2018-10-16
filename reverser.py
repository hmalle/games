
"""
A simple typing game that forces you to write the letters in reverse order
This enforces active engagement thats very important in learning new skills
"""

import pygame as pg
import sys, string,time
import random as rand

width, height = 800, 600

class Word():
    def __init__(self, char_count,font):
        self.width=0
        self.height=0
        self.x=rand.randint(0,width-self.width) #TODO: Minus word length box
        self.y=0
        self.text=generate_rand_word(char_count)
        self.width,self.height=font.size(self.text)
        self.color=self.get_color()
 
    #To change the color of the text in certain intervals
    def get_color(self):
        if self.y>(height*0.85):
            return "#ff0000"
        elif self.y>(height*0.65):
            return "#01baef"
        else:
            return "#000000"

    def is_past_height(self):
        if(self.y>height):
            return True
        else: 
            return False

    def update_word(self):
        self.y+=2    #Move the word 1 pixel down
        self.color=self.get_color()

class Player():
    def __init__(self):
        self.correct=0
        self.missed=0
        self.level=1
        self.time_interval=4
        self.char_count=5
        self.changed=False #To prevent levels adding up with every screen refresh

    def update(self):
        if (self.changed==True) and (self.correct!= 0 and self.correct%17==0) :
            self.level +=1
            self.changed=False
            self.char_count +=1

    def correct_answer(self):
        self.changed=True
        self.correct+=1

#Helper functions
def hex2rgb(hexcode):
    rgb = tuple(map(ord,hexcode[1:].decode('hex')))
    return rgb

def generate_rand_word(char_count):
    text=""
    for _ in range(char_count):
        text+=rand.choice(string.letters+string.digits)
    print("Genrated word "+text)
    return text.lower()

def print_wordlist(wordlist):
    for word in wordlist:
        print(word.text)

def remove_word(wordlist):
    for word in wordlist:
        wordlist.remove(word)
        break

#Main game function
def gamemain():
    fps=20
    #pg initializations
    pg.init()
    pg.font.init()
    font=pg.font.SysFont('monospace', 30)
    headerFont=pg.font.SysFont("monospace", 25)
    screen=pg.display.set_mode((width, height))
    pg.display.set_caption("revereserever")
    clock=pg.time.Clock()

    #The game loop
    start=time.time()
    player=Player()
    wordlist=[]
    wordlist.append(Word(player.char_count,font))
    user_word=""
    start=time.time()

    while True:
        for event in pg.event.get():
            if event.type==pg.QUIT:
                pg.font.quit()
                pg.quit()
                sys.exit()
            elif event.type==pg.KEYDOWN:
                key = event.key
                if key==pg.K_ESCAPE:
                    pg.font.quit()
                    pg.quit()
                    sys.exit()
                elif key==pg.K_RETURN or key==pg.K_SPACE: 
                    user_word=""    #Clear out the word entered by the user
                #Check the lower case asciis and the digits only
                elif(key>=97 and key<=122)or(key>=48 and key<=57):
                    user_word+=str(unichr(key))
                    #A little redundant code, but checks values without having to press RETURN
                    for word in wordlist:     
                        if word.text==user_word:
                            wordlist.remove(word)
                            player.correct_answer()
                            user_word=""
                elif event.key==pg.K_BACKSPACE:
                    #Enable deleting the last character when backspace is pressed
                    user_word=user_word[:-1]
                else:
                    pass
        screen.fill(hex2rgb("#000000"))
        #Generate a new word after every few seconds
        now=time.time()
        if now-start>=player.time_interval:
            start=time.time()
            wordlist.append(Word(char_count,font))

        #Render words on the screen and delete the missed past screen height
        for word in wordlist:
            if word.y > height:
                wordlist.remove(word)
                player.missed+=1
            else:
                text=font.render(word.text[::-1], True, hex2rgb(word.color))
                screen.blit(text,(word.x,word.y))
                word.update_word()    #Update here to avoid having anther loop
        player.update()
        #screen.blit(headerFont.render(("Level: "+str(player.level)),True,hex2rgb("#0affed"),(0,0)))

        screen.blit(headerFont.render(("Correct "+str(player.correct)), True, hex2rgb("#0000ff")),(0,20))
        pg.display.update()
        clock.tick(fps) #Frames per second

if __name__ == '__main__':
    gamemain()

