#=============================================================================#
#                                   library                                   #
import pygame
import saper
import maploader

pygame.init()
#=============================================================================#
#                                  settings                                   #
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
LEVEL_EAZY = saper.Saper_draft(9,20)

#=============================================================================#
#                                   *******                                   #

# draft = [[9, 1, 0, 0, 0, 1, 9, 1, 0],
#          [1, 2, 1, 1, 0, 1, 1, 1, 0],
#          [0, 2, 9, 2, 0, 0, 1, 1, 1],
#          [0, 2, 9, 3, 1, 0, 2, 9, 2],
#          [0, 1, 2, 9, 1, 0, 2, 9, 2],
#          [0, 0, 1, 2, 2, 1, 1, 1, 1],
#          [0, 0, 0, 2, 9, 2, 0, 0, 0],
#          [0, 0, 0, 2, 9, 2, 0, 1, 1],
#          [0, 0, 0, 1, 1, 1, 0, 1, 9]]

def array_printer(array:list):
        cols = len(array)
        for i in range(cols):
            print(array[i])

texture = {0:"0.png",1:"1.png",2:"2.png",3:"3.png",4:"4.png",5:"5.png",6:"6.png",7:"7.png",8:"8.png",9:"9.png"}
#=============================================================================#
#                                start set up                                 #
draft = LEVEL_EAZY.make_draft()
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('RPG-Life')
lodare = maploader.Maploader(SCREEN, (900,900), draft, (50,50))
lodare.set_texture(textures_paths = texture)
#=============================================================================#
array_printer(draft)
state = "start"
run = True
while run:
    SCREEN.fill((154, 205, 50))
    for event in pygame.event.get(): # Event handler
        if event.type == pygame.QUIT: # Quit game
            run = False

    lodare.draw_draft()
    pygame.display.update()

pygame.quit()
