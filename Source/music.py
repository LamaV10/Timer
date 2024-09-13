import pygame
from pygame import mixer

pygame.init()

def music():
    mixer.music.load("Music/It-was-a-good-day.mp3")
    mixer.music.set_volume(0.5)
    mixer.music.play(-1)
