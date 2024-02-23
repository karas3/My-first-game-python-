from utils.Button import *
from utils.Screen_info import Screen_width
import socket
import pyperclip

class main_menu:
    def __init__(self):
        self.font = pygame.font.Font(None, 72)
        self.host_name = socket.gethostname()
        self.IP = socket.gethostbyname(self.host_name)

        self.title_rect = self.font.render("Title", False, "white")
        self.title_width = self.title_rect.get_width()
        self.title_as_surface = self.font.render("Title", False, "white")

        self.IP_rect = self.font.render(self.IP, False, "white")
        self.IP_text_width = self.IP_rect.get_width()
        self.IP_as_surface = self.font.render(self.IP, False, "white")

        self.text1_rect = self.font.render("server adress", False, "white")
        self.text1_width = self.text1_rect.get_width()
        self.text1_as_surface = self.font.render("server adress", False, "white")

        self.host = Button(Screen_width / 2 - 400 / 2, 350, 400, 100)
        self.host.Set_color("grey")
        self.host.Add_Text("host game", None, 36, "black")

        self.join = Button(Screen_width / 2 - 400 / 2, 500, 400, 100)
        self.join.Set_color("grey")
        self.join.Add_Text("join game", None, 36, "black")

        self.exit = Button(Screen_width / 2 - 400 / 2, 650, 400, 100)
        self.exit.Set_color("grey")
        self.exit.Add_Text("Exit", None, 36, "black")

        self.back = Button(150, 100, 200, 100)
        self.back.Set_color("grey")
        self.back.Add_Text("Go Back", None, 36, "black")

        self.copy = Button(1920 / 2 + self.IP_text_width - 30, 115, 150, 100)
        self.copy.Set_color("grey")
        self.copy.Add_Text("Copy", None, 36, "black")

        self.main_objects = [self.host, self.join, self.exit]
        self.host_objects = [self.back, self.copy]
        self.join_objects = [self.back]
        self.all_objects = [self.main_objects, self.host_objects, self.join_objects]

        self.host_open = False
        self.join_open = False

    def open(self):
        for arrays in self.all_objects:
            for button in arrays:
                if button.mouse_hovered():
                    button.Set_color("yellow")
                else:
                    button.Set_color("grey")

        if self.host.clicked():
            self.host_open = True
                
        if self.join.clicked():
            self.join_open = True

        
        if self.host_open == False and self.join_open == False:
            screen.blit(self.title_as_surface, (1920 / 2 - self.title_width / 2, 150))

            for buttons in self.main_objects:
                buttons.draw()
            



        if self.host_open == True:
            screen.blit(self.text1_as_surface, (1920 / 2 - self.text1_width / 2, 100))
            screen.blit(self.IP_as_surface, (1920 / 2 - self.IP_text_width / 2, 170))

            for buttons in self.host_objects:
                buttons.draw()

            if self.back.clicked():
                self.host_open = False
                pass

            if self.copy.clicked():
                pyperclip.copy(self.IP)

        if self.join_open == True:
            for buttons in self.join_objects:
                buttons.draw()

            if self.back.clicked():
                self.join_open = False


    def user_wants_to_exit(self):
        if self.exit.clicked():
            return False
        else:
            return True

