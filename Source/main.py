import time
import math
import pygame
import music
from pygame import mixer

pygame.init()

stop = 0

#amount of time is being set
delay = float(input("Minutes: "))
delay = delay * 60
unix_time_diff = time.time() + delay
current_time = time.time()


run = True 
while run:
    # music import/play
    current_time = time.time()
    printTime = unix_time_diff - current_time

    if current_time > unix_time_diff:
        music.music()

    if current_time > unix_time_diff:
        stop = int(input("Type 1 and press enter to stop the timer: "))

    if stop == 1:
        run = False 
    
    if printTime <= 60:
        print(printTime, "s")

    if printTime > 60:
        print(printTime / 60, "min")
