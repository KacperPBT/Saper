#=============================================================================#
#                                   library                                   #
import pygame
import time
#=============================================================================#
#                                Ui like Button                               #
class Button():
    Surface = pygame.surface.Surface
    def __init__(self, 
                 coordinates : tuple,
                 image1: Surface | str,
                 image2: Surface | str = None,
                 image3: Surface | str = None,
                 scale : float = 1) -> None:
        if not image2:
            image2 = image1
        if not image3:
            if image2:
                image3 = image2
            else:
                image3 = image1
        if type(image1) == str:
            image1 = pygame.image.load(image1)
            image2 = pygame.image.load(image2)
            image3 = pygame.image.load(image3)
        width = image1.get_width()
        height = image1.get_height()
        self.image1 = pygame.transform.scale(image1, (int(width * scale),
                                                      int(height * scale)))
        self.image2 = pygame.transform.scale(image2, (int(width * scale),
                                                      int(height * scale)))
        self.image3 = pygame.transform.scale(image3, (int(width * scale),
                                                      int(height * scale)))
        self.rect = self.image1.get_rect()
        self.rect.topleft = coordinates
        self.clicked_l = False
        self.clicked_r = False
        self.clicked_a = False
    #=========================================================================#
    #                       Affects on left mouse clicks                      #
    def draw_l(self, surface : Surface, blocker : bool = False) -> bool: 
        action = False
        pos = pygame.mouse.get_pos() # Mouse position
        
        if not self.clicked_l:
            surface.blit(self.image1, (self.rect.x, self.rect.y))        
        
        if self.rect.collidepoint(pos) and not blocker:
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked_l:
                self.clicked_l = True
        
        if self.clicked_l:
            surface.blit(self.image2, (self.rect.x, self.rect.y))
            
        if pygame.mouse.get_pressed()[0] == 0 and self.clicked_l:
            self.clicked_l = False
            action = True
            time.sleep(0.3)

        return action
    #=========================================================================#
    #                      Affects on right mouse clicks                      #
    def draw_p(self, surface : Surface, blocker : bool = False) -> bool:
        action = False
        pos = pygame.mouse.get_pos() # Mouse position
        
        if not self.clicked_r:
            surface.blit(self.image1, (self.rect.x, self.rect.y))        
        
        if self.rect.collidepoint(pos) and not blocker:
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked_r:
                self.clicked_r = True
        
        if self.clicked_r:
            surface.blit(self.image2, (self.rect.x, self.rect.y))

        if pygame.mouse.get_pressed()[0] == 0 and self.clicked_r:
            self.clicked_r = False
            action = True
            time.sleep(0.3)

        return action
    #=========================================================================#
    #                       Affects on both mouse clicks                      #
    def draw_l_r(self, surface : Surface, blocker :bool = False) -> bool | str:
        action = False
        pos = pygame.mouse.get_pos() # Mouse position
        
        if not self.clicked_l and not self.clicked_r:
            surface.blit(self.image1, (self.rect.x, self.rect.y))   
        
        if self.rect.collidepoint(pos) and not blocker:
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked_a:
                self.clicked_a = True
                self.clicked_l = True
                self.clicked_r = False
                action = 'left'

            if pygame.mouse.get_pressed()[2] == 1 and not self.clicked_a:
                self.clicked_a = True
                self.clicked_r = True
                self.clicked_l = False
                action = 'right'

        if self.clicked_l:
            surface.blit(self.image2, (self.rect.x, self.rect.y))
        if self.clicked_r:
            surface.blit(self.image3, (self.rect.x, self.rect.y))
        
        return action   
#=============================================================================#
