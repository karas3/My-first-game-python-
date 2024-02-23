import pygame
from utils.Screen_info import screen , set_fps

class Button:
    #podstawowe parametry
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = ""
        self.text = ""
        self.frame_size = 0
        self.wait_for_next_input = 0
    #by dodać tekst
    def Add_Text(self, text, font, font_size, font_color):
        self.text = text
        self.font = font
        self.font_size = font_size
        self.font_color = font_color
    #by dodać ramkę
    def Add_Frame(self, size, color):
        self.frame_size = size
        self.frame_color = color
    #by wyświetlić
    def draw(self):
        if self.frame_size != 0 and self.color != "":
            #rysuje ramkę
            pygame.draw.rect(screen, self.frame_color, (self.x, self.y, self.width, self.height))
            #rysuje przycisk
            pygame.draw.rect(screen, self.color, (self.x + self.frame_size, self.y + self.frame_size, self.width - self.frame_size * 2, self.height - self.frame_size * 2))
        elif self.color != "":    
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        
        if self.text != "":
            font = pygame.font.Font(self.font, self.font_size)
            text_rect = font.render(self.text, False, self.font_color)
            #wyśrodkowuje tekst
            text_width, text_height = text_rect.get_size()
            text_as_surface = font.render(self.text, True, self.font_color)
            #wyświetla tekst
            screen.blit(text_as_surface, (self.x + self.width / 2 - text_width / 2, self.y + self.height / 2 - text_height / 2))

        if self.wait_for_next_input > 0:
            self.wait_for_next_input -= 1

    #by sprawdzić czy kliknięty
    def clicked(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        left_click, middle_click, right_click = pygame.mouse.get_pressed()
        if (self.x <= mouse_x <= self.x + self.width and self.y <= mouse_y <= self.y + self.height and left_click) and self.wait_for_next_input == 0:
            self.wait_for_next_input = round(set_fps / 6)
            return True
        else:
            return False
        
    def mouse_hovered(self):
         mouse_x, mouse_y = pygame.mouse.get_pos()
         if(self.x <= mouse_x <= self.x + self.width and self.y <= mouse_y <= self.y + self.height):
             return True
         else:
             return False
         
    def Get_color(self):
        return self.color
        

    def Set_text(self, value):
        self.text = value
    
    def Set_color(self, value):
        self.color = value

    def Set_font_color(self, value):
        self.font_color = value


        #jeśli przycisk ma być przeźroczysty to nie wystarczy mu nie ustawić kolor
        #jeśli przycisk nie ma mieć tesktu to go nie ustawiamy