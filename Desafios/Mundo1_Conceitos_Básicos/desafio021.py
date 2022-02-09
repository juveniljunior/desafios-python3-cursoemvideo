"""
Exercício Python 021:
Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
"""
'''import webbrowser
webbrowser.open('C:/Users/JUVENIL/PycharmProjects/Cursoemvideo/Desafios/WhatsApp Audio 2021 05 23 at 154339.mp3')'''

import pygame
pygame.mixer.init()
pygame.mixer.music.load('Ex021.wav')
pygame.mixer.music.play()
input()
pygame.event.wait()
