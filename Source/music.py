import pygame
from pygame import mixer
pygame.init()

def music():
      # music import/play
      # change your path to your music here:
      mixer.music.load('/home/lama/Music/Through The Fire And Flames.mp3')
      

      mixer.music.set_volume(0.5)
      mixer.music.play(-1)
