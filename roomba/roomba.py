# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 16:38:52 2020

@author: kim3
"""


from gpiozero import LED, Button
from playsound import playsound
from threading import Thread
import RPi.GPIO as gpio
import random
import time
import datetime
import sys

collisionbut = Button(2) # Pin 3
fuck = Button(3) # Pin 5
led = LED(17) # Pin 11

# "power" led
led.on()

# prepare gpio for motors
# Ref: https://maker.pro/raspberry-pi/tutorial/how-to-control-a-dc-motor-with-an-l298-controller-and-raspberry-pi
mode = gpio.getmode()
gpio.cleanup()
lfor = 27 # Pin 13
rfor = 22 # Pin 15
lbak = 23 # Pin 16
rbak = 24 # Pin 18
gpio.setmode(gpio.BOARD)
gpio.setup(lfor, gpio.OUT)
gpio.setup(rfor, gpio.OUT)
gpio.setup(lbak, gpio.OUT)
gpio.setup(rbak, gpio.OUT)


# initialize and logic for fuck button
def fuckbut():
    if fuck.is_pressed:
        print('fuck button triggered. halting execution')
        gpio.cleanup()
        return False
        sys.exit()
    else:
        return True
    
# Function to head left
def lefton(maxrt):
    time.sleep(500 / 1000)
    print('turning left')
    stop = datetime.datetime.now() + maxrt
    while datetime.datetime.now() < stop:
        print('turning left')
        # Put the code to turn Mykul left
        Thread(target = gpio.output(lbak, gpio.HIGH)).start()
        Thread(target = gpio.output(rfor, gpio.HIGH)).start()

# Function to head right
def righton(maxrt):
    time.sleep(500 / 1000)
    print('turning right')
    stop = datetime.datetime.now() + maxrt
    while (datetime.datetime.now() < stop):
        print('turning right')
        # Put the code to turn Mykul right
        Thread(target = gpio.output(lfor, gpio.HIGH)).start()
        Thread(target = gpio.output(rbak, gpio.HIGH)).start()

# Function to back dat ass up
def backwards(maxrt):
    time.sleep(500 / 1000)
    print('going backwards')
    stop = datetime.datetime.now() + maxrt
    while datetime.datetime.now() < stop:
        print('still going back')
        # Put the code to move the motors backwards here
        Thread(target = gpio.output(lbak, gpio.HIGH)).start()
        Thread(target = gpio.output(rbak, gpio.HIGH)).start()

# Function to move the robot forwards
# Move forwards until some event happens - this function doesn't handle collision logic
def forwards():
    time.sleep(500 / 1000)
    print('going forwards')
    Thread(target = gpio.output(lfor, gpio.HIGH)).start()
    Thread(target = gpio.output(rfor, gpio.HIGH)).start()

# Collision logic function
def collision():
    # STOP all motors
    gpio.output(lfor, gpio.LOW)
    gpio.output(rfor, gpio.LOW)
    # Ran into something - Mykul is in pain and suffering
    print('ah fuck i ran into something')
    owwie()
    # Back up from the 
    print('gotta back dat ass up')
    backwards(datetime.timedelta(seconds=0.5))
    print('hold on, turning')
    actionList = ['lefton(datetime.timedelta(seconds=0.2))', 'righton(datetime.timedelta(seconds=0.2))']
    random.choice(actionList)
    
# Function to play audio when Mykul bumps into something
def owwie():
    owList = ['ow1.mp3','ow2.mp3','ow3.mp3','ow4.mp3','ow5.mp3','ow6.mp3','ow7.mp3']
    playsound(random.choice(owList))
    time.sleep(1)

def main():
    runtime = True
    fuckbutstat = fuckbut()
    while (runtime == True and fuckbutstat == True):
        fuckbutstat = fuckbut()
        forwards()
        if collisionbut.is_pressed:
            collision()
            
if __name__ == "__main__":
    main()