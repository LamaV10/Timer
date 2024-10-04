import time
import math
import sys
import pygame
import music
from pygame import mixer

pygame.init()

stop = 0

def delete_last_line():
    "Use this function to delete the last line in the STDOUT"

    #cursor up one line
    sys.stdout.write('\x1b[1A')

    #delete last line
    sys.stdout.write('\x1b[2K')

#amount of time is being set
userDelay = float(input("Minutes: "))
delay = userDelay * 60
unix_time_diff = time.time() + delay 
current_time = time.time()

run = True 
while run:
    # music import/play
    current_time = time.time()

    leftoverTime = unix_time_diff - current_time
    printMinutes = leftoverTime / 60
    printSeconds = unix_time_diff - current_time
    secondsFromMinutes = round(userDelay) * 60

    if current_time > unix_time_diff:
        music.music()

    if current_time > unix_time_diff:
        stop = int(input("Type 1 and press enter to stop the timer: "))
    
    if leftoverTime <= 60:
        print(round(printSeconds, 1), "s")
        delete_last_line()

    if leftoverTime > 60:
        print(math.trunc(printMinutes),":", round(printSeconds - secondsFromMinutes), "min",)
        delete_last_line()

    if printSeconds - secondsFromMinutes < 0:
        userDelay = userDelay - 1

    if stop == 1:
        run = False 
