#
# A simple typing game that forces you to write the letters in reverse order
# This enforces active engagement thats very important in learning new skills
#

import pygame

pygame.init()
pygame.font.init()
my_font=pygame.font.SysFont('Comic Sans MS', 30)
clock=pygame.time.Clock()

#colors
blue=(0,128,255)
black=(0,0,0)

#costant variables
width =600
height=400
blockwidth=100
blockhehght=30


screen=pygame.display.set_mode((width, height))
pygame.display.set_caption("reverser")
done=False

while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN and event.key==pygame.K_RETURN:
            pass
            
    #Fonts testing
    text_surface=my_font.render("Hellow World", False, black)
    screen.blit(text_surface,(0,0))

    #Erase the screen
    screen.fill(black)
    my_rect=pygame.draw.rect(screen, blue, pygame.Rect(0, 0, width, 30))
    pygame.display.flip()
    clock.tick(30)
