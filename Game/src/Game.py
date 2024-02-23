import pygame
from utils.Screen_info import screen
from utils.objects import All_bakcground_objects

test_sprite = pygame.image.load('Resources/sprites/Sprite-0001.png').convert_alpha()

def run(dt, player):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        for obj in All_bakcground_objects:
            obj.Set_y(round(obj.Get_y() + player.Get_speed() * dt))

    if keys[pygame.K_s]:
        for obj in All_bakcground_objects:
            obj.Set_y(round(obj.Get_y() - player.Get_speed() * dt))

    if keys[pygame.K_a]:
        for obj in All_bakcground_objects:
            obj.Set_x(round(obj.Get_x() + player.Get_speed() * dt))

    if keys[pygame.K_d]:
        for obj in All_bakcground_objects:
            obj.Set_x(round(obj.Get_x() - player.Get_speed() * dt))

    #rysuje wszystkie obiekty
    for obj in All_bakcground_objects:
        pygame.draw.rect(screen, obj.Get_color(), (obj.Get_x(), obj.Get_y(), obj.Get_width(), obj.Get_height()))
    #wyświetla gracza
    #pygame.draw.rect(screen, "red", (player.Get_x(), player.Get_y(), player.Get_width(), player.Get_height()))
    screen.blit(test_sprite, (player.Get_x(), player.Get_y()))
    