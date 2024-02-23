import pygame
from utils.Screen_info import set_fps

class Single_press_key:
    def __init__(self, key):
        self.__key = key
        self.__wait_for_next_input = 0
        self.__pressed = False

    def Pressed(self):
        keys = pygame.key.get_pressed()
        
        if keys[self.__key] and self.__wait_for_next_input == 0:
            self.__wait_for_next_input = round(set_fps / 3)
            if self.__pressed == True:
                self.__pressed = False
            else:
                self.__pressed = True

        if self.__wait_for_next_input > 0:
            self.__wait_for_next_input -= 1

        return self.__pressed
    

#służy do tego żeby użyć klawisza 3 razy w ciągu sekundy max ,a nie np 60(gdyby nie to, to włączenie np inf o fps było by bardzo trudne i denerwujące)