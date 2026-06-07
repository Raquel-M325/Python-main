import pygame
pygame.init()
pygame.mixer_music.load('arquivo.mp3')
pygame.mixer_music.play()
pygame.event.wait()
