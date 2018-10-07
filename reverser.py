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

width =800
height=800

#Pygame initializations
pygame.init()
pygame.font.init()
font=pygame.font.SysFont('monospace', 30)
headerFont=pygame.font.SysFont("monospace", 25)
screen=pygame.display.set_mode((width, height))
pygame.display.set_caption("reverser")
clock=pygame.time.Clock()

class Word():
  #Variables
  x=0
  y=0
  text=""
  width=0
  height=0

  def __init__(self, char_count):
    self.text=self.generate_random_word(char_count)
    self.width,self.height=font.size(self.text)
    self.color=self.get_color()
    self.x=random.randint(0,width-self.width) #TODO: Minus word length box
    self.y=0
 
  #To change the color of the text in certain intervals
  def get_color(self):
    if self.y>(height*0.85):
      return red
    elif self.y>(height*0.65):
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

def print_wordlist(wordlist):
  for word in wordlist:
    print(word.text)

def remove_word(wordlist):
  for word in wordlist:
    wordlist.remove(word)
    break

def main():
  #The game loop
  done=False
  player=Player()
  char_count=5
  wordlist=[]
  wordlist.append(Word(player.char_count))
  user_word=""
  start=time.time()

  while not done:
    for event in pygame.event.get():
      if event.type==pygame.QUIT:
        pygame.font.quit()
        pygame.quit()
        sys.exit()
      #When the enter key is pressed, check the word thats been entered
      if event.type==pygame.KEYDOWN:
        if event.key==pygame.K_RETURN: #13
          for word in wordlist:
            if word.text==user_word:
              wordlist.remove(word)
              player.correct_answer()
          user_word=""
        #Check the lower case asciis and the digits only
        elif(event.key>=97 and event.key<=122)or(event.key>=48 and event.key<=57):
          user_word+=str(unichr(event.key))
          #A little redundant code, but checks values without having to press RETURN
          for word in wordlist:   
            if word.text==user_word:
              wordlist.remove(word)
              player.correct_answer()
              user_word=""
        elif event.key==pygame.K_BACKSPACE:
          #Enable deleting the last character when backspace is pressed
          user_word=user_word[:-1]
        else:
          pass
    screen.fill(black)
    #Generate a new word after every few seconds
    now=time.time()
    if now-start>=player.time_interval:
      start=time.time()
      wordlist.append(Word(char_count))

    #Render words on the screen and delete the missed past screen height
    for word in wordlist:
      if word.y > height:
        wordlist.remove(word)
        player.missed+=1
      else:
        text=font.render(word.text[::-1], True, word.color)
        screen.blit(text,(word.x,word.y))
        word.update_word()  #Update here to avoid having anther loop
    player.update()
    screen.blit(headerFont.render(("Level "+str(player.level)), True, blue),(0,0))
    #screen.blit(headerFont.render(("Correct "+str(player.correct)), True, blue),(0,20))
    pygame.display.update()

    clock.tick(20) #Frames per second

if __name__ == '__main__':
  main()

