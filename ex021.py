import pygame

pygame.mixer.init()
pygame.mixer_music.load('Overjoyed.mp3')
pygame.mixer_music.play()

while pygame.mixer_music.get_busy():
    pygame.time.Clock().tick(10)

