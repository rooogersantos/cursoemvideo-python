import pygame

pygame.init()
pygame.mixer.music.load('abracadabra_live_from_copacabana.mp3')
pygame.mixer.music.play()
pygame.event.wait()

input("Pressione ENTER para encerrar...")