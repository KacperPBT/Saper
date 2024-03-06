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
LEVEL_EAZY = saper.Saper_draft(8,10)
LEVEL_MEDIUM = saper.Saper_draft(16,40)
LEVEL_HARD = saper.Saper_draft((31,16),99)
TEXTURE = {0:"image/0.png",1:"image/1.png",2:"image/2.png",3:"image/3.png",4:"image/4.png",
           5:"image/5.png",6:"image/6.png",7:"image/7.png",8:"image/8.png",9:"image/9.png"}
#=============================================================================#
#                                start set up                                 #
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Saper')
draft = LEVEL_EAZY.make_draft()
loader = maploader.Maploader(SCREEN, (900,900), draft, (50,50))
loader.set_texture(textures_paths = TEXTURE)

#=============================================================================#
# loader.draw_draft()

state = "lvl eazy"
run = True
while run:
    SCREEN.fill((154, 205, 50))
    for event in pygame.event.get(): # Event handler
        if event.type == pygame.QUIT: # Quit game
            run = False
    if state == "start":




        if state == "lvl eazy": # to na końcu 
            draft = LEVEL_EAZY.make_draft()
            loader.set_draft(draft)

        if state == "lvl medium": 
            draft = LEVEL_MEDIUM.make_draft()
            loader.set_draft(draft)

        if state == "lvl hard": 
            draft = LEVEL_HARD.make_draft()
            loader.set_draft(draft)
    

    if state == "lvl eazy":  # Dla poziomu łatwy
        loader.draw_draft()

    if state == "lvl medium":# Dla poziomu średni
        loader.draw_draft()

    if state == "lvl hard":  # Dla poziomu trudny
        loader.draw_draft()

    pygame.display.update()

pygame.quit()