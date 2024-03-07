#=============================================================================#
#                                   library                                   #
import pygame
import time
#=============================================================================#
#                               rendered imagine                              #
class Button():
    def __init__(self,
                 x : int,
                 y : int,
                 image1,
                 image2 = None,
                 image3 = None,
                 scale : float = 1) -> None:
        
        width = image1.get_width()
        height = image1.get_height()
        self.image1 = pygame.transform.scale(image1, (int(width * scale),
                                                      int(height * scale)))
        if image2:
            self.image2 = pygame.transform.scale(image2, (int(width * scale),
                                                          int(height * scale)))
        else:
            self.image2 = pygame.transform.scale(image1, (int(width * scale),
                                                          int(height * scale)))
        if image3:
            self.image3 = pygame.transform.scale(image3, (int(width * scale),
                                                          int(height * scale)))
        elif image2:
            self.image3 = pygame.transform.scale(image2, (int(width * scale),
                                                          int(height * scale)))
        else:
            self.image3 = pygame.transform.scale(image1, (int(width * scale),
                                                          int(height * scale)))  
        self.rect = self.image1.get_rect()
        self.rect.topleft = (x, y)
        self.clicked_l = False
        self.clicked_r = False
        self.clicked_a = False

    # affects on left mouse clicks
    def draw_l(self, surface, blocker : bool = False): 
        action = False
        pos = pygame.mouse.get_pos() # Mouse position
        
        if self.clicked_l == False:
            surface.blit(self.image1, (self.rect.x, self.rect.y))        
        
        if self.rect.collidepoint(pos) and not blocker:
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked_l:
                self.clicked_l = True
        
        if self.clicked_l == True:
            surface.blit(self.image2, (self.rect.x, self.rect.y))
            

        if pygame.mouse.get_pressed()[0] == 0 and self.clicked_l:
            self.clicked_l = False
            action = True
            time.sleep(0.3)

        return action
    
    # affects on right mouse clicks
    def draw_p(self, surface, blocker : bool = False) -> bool:
        action = False
        pos = pygame.mouse.get_pos() # Pozycja myszki
        
        if self.clicked_r == False:
            surface.blit(self.image1, (self.rect.x, self.rect.y))        
        
        if self.rect.collidepoint(pos) and not blocker:
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked_r:
                self.clicked_r = True
        
        if self.clicked_r == True:
            surface.blit(self.image2, (self.rect.x, self.rect.y))
            

        if pygame.mouse.get_pressed()[0] == 0 and self.clicked_r:
            self.clicked_r = False
            action = True
            time.sleep(0.3)

        return action
    
    # affects on both mouse clicks    
    def draw_l_r(self, surface, blocker :bool = False):
        action = False
        pos = pygame.mouse.get_pos() # Pozycja myszki
        
        if self.clicked_l == False:
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

        if self.clicked_l == True:
            surface.blit(self.image2, (self.rect.x, self.rect.y))
        if self.clicked_r == True:
            surface.blit(self.image3, (self.rect.x, self.rect.y))

        
        return action
    
#=============================================================================#
#                               imagine by path                               #
class ButtonF():
    def __init__(self,
                 x : int,
                 y : int,
                 image1_path,
                 image2_path = None,
                 image3_path = None,
                 scale : float = 1) -> None:
        
        image1 = pygame.image.load(image1_path)
        if image2_path:
            image2 = pygame.image.load(image2_path)
        else:
            image2 = None
        if image3_path:
            image3 = pygame.image.load(image3_path)
        else:
            image3 = None
        width = image1.get_width()
        height = image1.get_height()
        self.image1 = pygame.transform.scale(image1, (int(width * scale),
                                                      int(height * scale)))
        if image2:
            self.image2 = pygame.transform.scale(image2, (int(width * scale),
                                                          int(height * scale)))
        else:
            self.image2 = pygame.transform.scale(image1, (int(width * scale),
                                                          int(height * scale)))
        if image3:
            self.image3 = pygame.transform.scale(image3, (int(width * scale),
                                                          int(height * scale)))
        else:
            self.image3 = pygame.transform.scale(image2, (int(width * scale),
                                                          int(height * scale)))
        self.rect = self.image1.get_rect()
        self.rect.topleft = (x, y)
        self.clicked_l = False
        self.clicked_r = False

    # affects on left mouse clicks
    def draw_l(self, surface, blocker : bool = False) -> bool: 
        action = False
        pos = pygame.mouse.get_pos() # Mouse position
        
        if self.clicked_l == False:
            surface.blit(self.image1, (self.rect.x, self.rect.y))        
        
        if self.rect.collidepoint(pos) and not blocker:
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked_l:
                self.clicked_l = True
        
        if self.clicked_l == True:
            surface.blit(self.image2, (self.rect.x, self.rect.y))
            

        if pygame.mouse.get_pressed()[0] == 0 and self.clicked_l:
            self.clicked_l = False
            action = True
            time.sleep(0.3)

        return action
    
    # affects on right mouse clicks
    def draw_p(self, surface, blocker : bool = False) -> bool:
        action = False
        pos = pygame.mouse.get_pos() # Pozycja myszki
        
        if self.clicked_r == False:
            surface.blit(self.image1, (self.rect.x, self.rect.y))        
        
        if self.rect.collidepoint(pos) and not blocker:
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked_r:
                self.clicked_r = True
        
        if self.clicked_r == True:
            surface.blit(self.image2, (self.rect.x, self.rect.y))
            

        if pygame.mouse.get_pressed()[0] == 0 and self.clicked_r:
            self.clicked_r = False
            action = True
            time.sleep(0.3)

        return action
    
    # affects on both mouse clicks
    def draw_l_r(self, surface, blocker : bool = False):
        action = False
        pos = pygame.mouse.get_pos() # Pozycja myszki
        
        if self.clicked_l == False:
            surface.blit(self.image1, (self.rect.x, self.rect.y))   
        
        if self.rect.collidepoint(pos) and not blocker:
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked_a:
                self.clicked_a = True
                self.clicked_l = True
                action = 'left'

            if pygame.mouse.get_pressed()[2] == 1 and not self.clicked_a:
                self.clicked_a = True
                self.clicked_r = True
                action = 'right'

        if self.clicked_l == True:
            surface.blit(self.image2, (self.rect.x, self.rect.y))
        if self.clicked_r == True:
            surface.blit(self.image3, (self.rect.x, self.rect.y))

        
        return action
#=============================================================================#
