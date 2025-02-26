import pygame
from pygame import mixer
pygame.init()

def music():
      # music import/play
      # change your path to your music here:
      mixer.music.load('/home/marcel/Documents/IT/Python/Timer/Source/Music/Flashing-Lights.mp3')
      

      mixer.music.set_volume(0.5)
      mixer.music.play(-1)
