#=============================================================================#
#                                   library                                   #
import pygame
import button
#=============================================================================#
class Maploader:
    def __init__(self, surface, display_size : tuple, draft : list,
                 coordinate : tuple = (0,0)) -> None:
        self.surface = surface
        self.display_size = display_size
        self.draft = draft
        width  = display_size[0] / len(draft[0])
        height = display_size[1] / len(draft)
        self.size = (width, height)
        self.coordinate = coordinate
        self.evry_coordinate = self.calculate_location()
        self.clicked_draft = array_filler(len(self.draft),len(self.draft[0]), False)
        self.buttons_created = False
    #=========================================================================#
    #                              Set new draft                              #
    def set_draft(self, draft : list) -> None:
        self.draft = draft
        width  = self.display_size[0] / len(draft[0])
        height = self.display_size[1] / len(draft)
        self.size = (width, height)
        self.evry_coordinate = self.calculate_location()
        self.clicked_draft = array_filler(len(self.draft),len(self.draft[0]), False)
        self.buttons_created = False
    #=========================================================================#
    #                       Set textures for your draft                       #
    def set_texture(self, loaded_textures : dict = None, textures_paths : dict = None) -> dict:
        self.textures = {}
        if loaded_textures and textures_paths:
            raise TypeError("Function set_texture takes 1 argument but 2 were given")
        elif not loaded_textures and not textures_paths:
            raise TypeError("Function set_texture missing 1 required argument")
        elif loaded_textures:
            self.textures = loaded_textures
        elif textures_paths:
            for id, path in textures_paths.items():
                self.textures[id] = pygame.image.load(path)
        for i in range(len(self.draft)):
            for j in range(len(self.draft[i])):
                if self.draft[i][j] == None:
                    continue
                trigger = False
                for id in self.textures.items():
                    if self.draft[i][j] == id[0]:
                        trigger = True
                        break
                if trigger == False:
                    raise ValueError(f'At least one texture is missing "{self.draft[i][j]}"')
        self.buttons_created = False
        return self.textures
    #=========================================================================#
    #                     Draw your draft as olny texture                     #
    def draw_draft(self):
        for i in range(len(self.draft)):
            for j in range(len(self.draft[i])):
                if self.draft[i][j] == None:
                    continue
                rect = self.textures[self.draft[i][j]].get_rect()
                rect.topleft = self.evry_coordinate[i][j]
                self.surface.blit(self.textures[self.draft[i][j]], 
                                  (rect.x, rect.y))
    #=========================================================================#
    #            Initialize evry element of your draft as "buttons"           #
    def button_init(self) -> bool:
        if self.buttons_created:
            return True
        self.buttons = array_filler(len(self.draft),len(self.draft[0]), 0)
        for i in range(len(self.draft)):
            for j in range(len(self.draft[i])):
                if self.draft[i][j] == None:
                    continue
                self.buttons[i][j] = button.Button(self.evry_coordinate[i][j],
                                                   self.textures["hidden"],
                                                   self.textures[self.draft[i][j]],
                                                   self.textures["flag"],
                                                   0.09765625)
        self.buttons_created = True
        return True
    #=========================================================================#
    #         Draw your draft as "buttons" (interact on mouse clicks)         #
    def draw_draft_b(self):
        self.button_init()
        for i in range(len(self.draft)):
            for j in range(len(self.draft[i])):
                if self.draft[i][j] == None:
                    continue
                square = self.buttons[i][j].draw_l_r(self.surface)
                self.buttons[i][j].clicked_a = False
                if square != False:
                    self.clicked_draft[i][j] = square
               
    def calculate_location(self) -> list[tuple]:
        evry_coordinate = array_filler(len(self.draft),len(self.draft[0]),0)
        for i in range(0,len(self.draft)):
            for j in range(0,len(self.draft[i])):
                evry_coordinate[i][j] = (int(self.coordinate[0] + j * self.size[0]),
                                         int(self.coordinate[1] + i * self.size[1]))  
        return evry_coordinate

def array_filler(cols : int, rows : int, filer) -> list:
    array = []
    for _ in range(cols):
        sub_array = []
        for _ in range(rows):
            sub_array.append(filer)
        array.append(sub_array)
    return array   