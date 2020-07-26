# -*- coding: utf-8 -*-
"""
Created on Sun Jul 27 16:47:52 2020

@author: kim3
"""

from gpiozero import LED, Button
from playsound import playsound
import time
import sys
import random

collisionbut = Button(2) # Pin 3
fuck = Button(3) # Pin 5
led = LED(17)

# initialize and logic for fuck button
def fuckbut():
    if fuck.is_pressed:
        print('fuck button triggered. halting execution.')
        return False
        sys.exit()
    else:
        return True

# "power" led flash
led.blink()

print('Motors should not engage. Test collisions manually only.')
print('Do not engage motors manually.')

# Collision logic function
def collision():
    print('collision detected')
    owwie()

def owwie():
    print('ow i am in pain and suffering')
    owList = ['./testaudio/testOw1.mp3', './testaudio/testOw2.mp3', './testaudio/testOw3.mp3']
    playsound(random.choice(owList))
    time.sleep(1)

def main():
    runtime = True
    fuckbutstat = fuckbut()
    while (runtime == True and fuckbutstat == True):
        fuckbutstat = fuckbut()
        print('Waiting for input')
        if collisionbut.is_pressed:
            collision()
