#=============================================================================#
#                                   library                                   #
import pygame
#=============================================================================#
class Maploader:
    def __init__(self, surface, display_size : tuple, draft : list, coordinate : tuple = (0,0)) -> None:
        self.surface = surface
        self.display_size = display_size
        self.draft = draft
        width  = display_size[0] / len(draft[1])
        height = display_size[1] / len(draft[0])
        self.size = (width, height)
        self.coordinate = coordinate

    def set_draft(self, draft : list) -> None:
        self.draft = draft
        width  = self.display_size[0] / len(draft[1])
        height = self.display_size[1] / len(draft[0])
        self.size = (width, height)

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
        '''for entry in self.draft.items():
            trigger = False
            for id in self.textures.items():
                if entry == id:
                    trigger = True
                    break
            if trigger == False:
                raise ValueError("At least one texture is missing")'''
        return self.textures

    def draw_draft(self):
        self.evry_coordinate = calculate_location(self.draft, self.coordinate, self.size)
        for i in range(len(self.draft)):
            for j in range(len(self.draft[i])):
                rect = self.textures[self.draft[i][j]].get_rect()
                rect.topleft = calculate_location(self.draft, self.coordinate, self.size)[i][j]
                self.surface.blit(self.textures[self.draft[i][j]], (rect.x, rect.y))

def array_filler(cols : int, rows : int, filer) -> list:
    array = []
    for i in range(cols):
        sub_array = []
        for j in range(rows):
            sub_array.append(filer)
        array.append(sub_array)
    return array               
                
def calculate_location(draft : list, coordinate : tuple, size : tuple) -> list[tuple]:
    evry_coordinate = array_filler(9,9,0)
    for i in range(0,len(draft)):
        for j in range(0,len(draft[i])):
            evry_coordinate[i][j] = (int(coordinate[0] + j * size[0]), int(coordinate[1] + i * size[1]))  
    return evry_coordinate
