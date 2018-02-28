#!/usr/bin/env python
# coding: latin-1
# Autor:   Ingmar Stapel
# Datum:   20180228
# Version:   1.0
# Homepage:   http://custom-build-robots.com
# I developed this program to control a normal
# RC car wiht a steering servo and a ESC.

# Import of the Adafruit PCA9685 library for the
# PCA9685 servo controller.
import Adafruit_PCA9685

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()

# import some python funciton which are used 
import time, curses, sys, os

# Set the PWM frequency for to control the servo and ESC.
# Some ESCs need a 50er frequency to work
pwm.set_pwm_freq(60)

# set the screen with the library cruses to display some
# informations like speed and steering angle.
screen = curses.initscr()
curses.noecho()
curses.cbreak()

screen.keypad(True)

# This sections sets the default values for the ESC
running = True
fwdmax = 600
revmax = 200
inc = 20
spinup = 1
# the value 400 is the value my ESC accepts as no throttle
# set. This value is not always 400. The value is used to
# to stop and to seitch between forward / reverse.
stop = 400
go = 400
# This section sets the default values for the 
# steering servo. Depending of your servo an how it is mounted
# you have to changes those values.
steering_value = 500
steering_value_init = steering_value
steering_max_left = 380
steering_max_right = 620

def printscreen():
        # The command os.system('clear') clears the screen.
        os.system('clear')
        print("============ RC car controller ============\r")
        print(u"\u2191/\u2193: accelerate/brake\r")
        print(u"\u2190/\u2192: left/right\r")
        print("q:   stops the motor\r")
        print("x:   exit the program\r")
        print("b:   boot the esc\r")        
        print("============== speed display ==============\r")
        print("speed dc motor: "+str(go-stop)+"\r")
        print("steering angle: "+str(steering_value-steering_value_init)+"\r")

# function to boot the esc
def bootup():
    boot = 200
    while boot < fwdmax:
        boot += inc
        pwm.set_pwm(0,0,boot)
        time.sleep(0.1)
        if boot > fwdmax:
            while boot > revmax:
                 boot -= inc
                 pwm.set_pwm(0,0,boot)
                 time.sleep(0.1)
                 if boot < revmax:
                     boot = 400
                     pwm.set_pwm(0,0,boot)
                     spinup = 0
                     break
# program loop to control the RC car via a keyboard.
while running:
    printscreen()
    char = screen.getch()
    # stopp the dc motor
    if char == ord('q'):
            go = stop
            steering_value = steering_value_init
    # boot the esc
    elif char == ('b') and spinup == 1:
        bootup()
    # end the program
    elif char == ord('x'):
        go = stop
        steering_value =  steering_value_init
        print("Program Ended\r")
        time.sleep(1)
        running=False
    # accelerate drive forward
    elif char == curses.KEY_UP:
            if go == 400:
                time.sleep(0.2)
            if go < fwdmax:
                    go += inc
    # brake and drive backwards
    elif char == curses.KEY_DOWN:
            if go == 400:
                time.sleep(0.2)        
            if go > revmax:
                    go -= inc
    # steer left
    elif char == curses.KEY_LEFT:
            steering_value = steering_value - 10
            if steering_value > steering_value_init:
                steering_value = steering_value_init                
            if steering_value < steering_max_left:
                    steering_value = steering_max_left     
    # steer right                   
    elif char == curses.KEY_RIGHT:                       
            steering_value = steering_value + 10
            if steering_value < steering_value_init:
                steering_value = steering_value_init                 
            if steering_value > steering_max_right:
                    steering_value = steering_max_right
    # print the scrren with the latest values
    printscreen()
    # set the PCA9685 servo controller (dc motor and 
    # steering servo)
    pwm.set_pwm(0, 0, go)
    pwm.set_pwm(1, 0, steering_value)

# shut down the program and clean up everything
curses.nocbreak(); screen.keypad(0); curses.echo()
curses.endwin()
