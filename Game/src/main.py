import pygame
import sys
import time
import Main_menu
import Game
from Player import Player
from utils.Screen_info import screen, set_fps
from utils.Single_press_keys import Single_press_key

main_menu_instance = Main_menu.main_menu()

#inicjalizacja pygame
pygame.init()

#podstawowe parametry (większość zostanie przeniesiona gdzieś indziej)
tick = 0
fps = 0
Main_menu_opened = True
Game_opened = False
player = Player()

#inicjalizacja niektórych klawiszy których się ciągle nie używana tak jak np wsad
F3_key = Single_press_key(pygame.K_F3)
ESC_key = Single_press_key(pygame.K_ESCAPE)
#zapis tych klawiszy w liście by użyć pojedyńczej pętli do operowania nimi
All_single_press_keys = [
    F3_key,
    ESC_key]

#inicjalizacja zegara
clock = pygame.time.Clock()
#służy do wyświetlania danych takich jak fps itd... (wystarczy podać rodzaj danych i ich pozycje na ekranie)
def Display_data(data, pos):
    font = pygame.font.Font(None, 36)
    screen.blit(font.render(data, False, "white"), pos)
running = True
#poprzedni czas (potrzebne by wyliczyć fps)
previous_time = time.time()
while running:
    #delta czasu (potrzebne by wyliczyć fps)
    dt = time.time() - previous_time
    previous_time = time.time()
    #odświeża ekran
    screen.fill((0, 0, 0)) 

    if Main_menu_opened:
        main_menu_instance.open()
        running = main_menu_instance.user_wants_to_exit() #True/False

    #sprawdza czy X był kliknięty (można by to było usunąć bo zawsze jest alt-f4)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if ESC_key.Pressed():
        running = False       
        
    #wyświetla fps itd...
    if F3_key.Pressed():
        Display_data(f"FPS: {fps}", (player.Get_x() - 930, player.Get_y() - 510))
        if dt > 0 and tick % (set_fps / 2) == 0:
            fps = round(1 / dt)

    #potrzebne po to by fps były czytelne (prawdopodbnie kiedyś to przebuduje)
    tick += 1
    if tick == set_fps:
        tick = 0
    
    pygame.display.flip()
    clock.tick(set_fps)

# Quit Pygame
pygame.quit()
sys.exit