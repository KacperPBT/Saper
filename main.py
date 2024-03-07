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
TEXTURE = {0:"image/0.png",1:"image/1.png",2:"image/2.png",3:"image/3.png",
           4:"image/4.png",5:"image/5.png",6:"image/6.png",7:"image/7.png",
           8:"image/8.png",9:"image/9.png","right":"image/right.png",
           "hidden":"image/hidden.png"}
#=============================================================================#
#                                start set up                                 #
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Saper')
draft = LEVEL_EAZY.make_draft()
loader = maploader.Maploader(SCREEN, (900,900), draft, (50,50))
loader.set_texture(textures_paths = TEXTURE)

#=============================================================================#
#                                  Game loop                                  #
state = "lvl eazy"
run = True
while run:
    SCREEN.fill((154, 205, 50))
    #=========================================================================#
    #                              Event handler                              #
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Quit game
            run = False
    #=========================================================================#
    #                               Start window                              #
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
    #=========================================================================#
    #                                level eazy                               #
    if state == "lvl eazy": 
        loader.draw_draft_b()
    #=========================================================================#
    #                               level medium                              #
    if state == "lvl medium":
        loader.draw_draft_b()
    #=========================================================================#
    #                                level hard                               #
    if state == "lvl hard":
        loader.draw_draft_b()
    #=========================================================================#
    #                               end of loop                               #
    pygame.display.update()
print(loader.clicked_draft)

pygame.quit()
#=============================================================================#