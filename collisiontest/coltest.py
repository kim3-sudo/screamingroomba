# -*- coding: utf-8 -*-
"""
Created on Sun Jul 27 16:47:52 2020

@author: kim3
"""

from gpiozero import LED, Button
from playsound import playsound
import time
import sys

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
led.blink() #should probably move this to main

print('Motors should not engage. Test collisions manually only.') #move this chunk to main too
print('Do not engage motors manually.')
print('fuck button probably doesn\'t work because fuck you')

def owwie1():
    print('ow i am in pain and suffering')
    playsound('./testaudio/testOw1.mp3')
    time.sleep(1)

def owwie2():
    print('existance is pain')
    playsound('./testaudio/testOw2.mp3')
    time.sleep(1)

def owwie3():
    print('fuck you')
    playsound('./testaudio/testOw3.mp3')
    time.sleep(1)

def main():
    runtime1 = True
    while (runtime1 == True):
        print('Waiting for input')
        if collisionbut.is_pressed:
            print('collision detected')
            owwie1()
            runtime1 = False
    runtime2 = True
    while (runtime2 == True):
        print('Waiting for input')
        if collisionbut.is_pressed:
            print('collision detected')
            owwie2()
            runtime2 = False
    runtime3 = True
    while (runtime3 == True):
        print('Waiting for input')
        if collisionbut.is_pressed:
            print('collision detected')
            owwie3()
            runtime3 = False
    print('im done shittertons')
