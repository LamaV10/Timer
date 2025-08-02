import time
import math
import sys
import pygame
import music

pygame.init()

def delete_last_line():
    # Cursor up one line.
    sys.stdout.write('\x1b[1A')

    # Delete last line.
    sys.stdout.write('\x1b[2K')

stop = 0
# Amount of time is being set.
userDelay = float(input("Minutes: "))
# Full minutes that are left over.
fullMinutes = math.trunc(userDelay)
# From minutes into seconds.
delay = userDelay * 60
# Unix time + the delay the user wants.
unix_time_wanted = time.time() + delay

run = True
while run:
    # current unix time
    current_time = time.time()

    # Leftover time in seconds between unix time and the desiered user time.
    leftoverTime = unix_time_wanted - current_time
    # Minutes that are left over rounded down to have no decimel places!
    printMinutes = math.trunc(leftoverTime / 60)
    # Minutes rounded down & multiplied by 60 to get the seconds from the full minutes.
    # This is being subtracted from the total seconds to get the leftover seconds from the current minute.
    secondsFromMinutes = (math.trunc(leftoverTime) - (fullMinutes * 60))

    if current_time >= unix_time_wanted:
        music.music()
        stop = int(input("Type 1 and press enter to stop the timer: "))

    # Prints seconds if the there are no more full minutes left.
    if leftoverTime <= 60:
        print(round(leftoverTime, 1), "s")
        delete_last_line()

    # Prints minutes and seconds (min : sec) when there are still full minutes left.
    elif leftoverTime > 60:
        print((printMinutes), ":", (secondsFromMinutes), "min", )
        delete_last_line()

    # When a full minute is up this fullMinutes variable is being subtracted by 1. This is important for the secondsFromMinutes calculation!
    if secondsFromMinutes < 0:
        fullMinutes -= 1

    if stop == 1:
        run = False
    time.sleep(0.1)


