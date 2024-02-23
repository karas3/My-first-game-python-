import pygame

pygame.init()

Screen_width, Screen_height = pygame.display.Info().current_w, pygame.display.Info().current_h
screen = pygame.display.set_mode((Screen_width, Screen_height))

set_fps = 60

pygame.display.set_caption("Game")