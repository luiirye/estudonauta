# Faça um programa em Python que abre e reproduza o áudio de arquivo MP3

import pygame
import time

pygame.init() #Iniciando o pygame
pygame.mixer.music.load('desafio21.mp3')
pygame.mixes.music.play()
pygame.event.wait()