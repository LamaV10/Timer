import pygame
from pygame import mixer
pygame.init()

def music():
      # music import/play
      # change your path to your music here:
      mixer.music.load('/home/lama/Music/Alt-Rap/Larry June, The Alchemist - 60 Days.mp3')
      

      mixer.music.set_volume(0.5)
      mixer.music.play(-1)
