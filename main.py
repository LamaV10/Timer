import time
import math
import pygame
import pyautogui as auto
from pygame import mixer

pygame.init()
pygame.mixer.init()


timer = float(input("Minuten: "))
timer = timer * 60

time.sleep(timer)
auto.write("1")

run = True 
while run:
    # music import/play
    mixer.music.load("Music/Meat-Grinder.mp3")
    mixer.music.set_volume(0.5)
    mixer.music.play(-1)
    
    
    stop = int(input(auto.write("1")))
    if stop == 1:
        run = False 
