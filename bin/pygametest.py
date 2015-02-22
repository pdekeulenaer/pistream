import pygame.mixer.music

f1 = 'file1.wav'
f2 = 'file2.wav'

pygame.mixer.init()

pygame.mixer.music.load(f1)
pygame.mixer.music.queue(f2)

pygame.mixer.music.play()