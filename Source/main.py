import time
import math
import pygame

import music
from pygame import mixer

pygame.init()
# pygame.mixer.init()

stop = 0

timer = float(input("Minuten: "))
timer = timer * 60

time.sleep(timer)

run = True 
while run:
    # music import/play
    music.music()    
    stop = int(input("Type 1 and press enter to stop the timer: "))
        
    if stop == 1:
        run = False 
