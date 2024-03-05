#=============================================================================#
#                                   library                                   #
import pygame
import maploader

pygame.init()
#=============================================================================#
#                                  settings                                   #
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000

#=============================================================================#
#                                   *******                                   #
draft = [[9, 1, 0, 0, 0, 1, 9, 1, 0],
         [1, 2, 1, 1, 0, 1, 1, 1, 0],
         [0, 2, 9, 2, 0, 0, 1, 1, 1],
         [0, 2, 9, 3, 1, 0, 2, 9, 2],
         [0, 1, 2, 9, 1, 0, 2, 9, 2],
         [0, 0, 1, 2, 2, 1, 1, 1, 1],
         [0, 0, 0, 2, 9, 2, 0, 0, 0],
         [0, 0, 0, 2, 9, 2, 0, 1, 1],
         [0, 0, 0, 1, 1, 1, 0, 1, 9]]

# [[0, 0, 0, 0, 1, 9, 1, 0, 0],
#  [1, 1, 1, 0, 1, 1, 1, 0, 0],
#  [1, 9, 1, 0, 1, 1, 1, 0, 0],
#  [1, 1, 1, 0, 1, 9, 1, 0, 0],
#  [0, 0, 0, 0, 1, 2, 2, 1, 0],
#  [0, 1, 1, 2, 1, 2, 9, 1, 0],
#  [1, 2, 9, 4, 9, 4, 2, 2, 0],
#  [1, 9, 3, 9, 9, 3, 9, 1, 0],
#  [1, 1, 2, 2, 2, 2, 1, 1, 0]]

texture = {0:"0.png",1:"1.png",2:"2.png",3:"3.png",4:"4.png",5:"5.png",6:"6.png",7:"7.png",8:"8.png",9:"9.png"}
#=============================================================================#
#                                start set up                                 #
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('RPG-Life')
lodare = maploader.Maploader(SCREEN, (900,900), draft, (50,50))
lodare.set_texture(textures_paths = texture)
#=============================================================================#

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
