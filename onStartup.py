# onStartup.py
# Authors: Julia Zelevinsky and Anna Quiros
# CEEO Summer Interns 2022
# Purpose: Activate indicator lights on the PiHub using GPIO pins
# on the Raspberry Pi 4. The startup_led turns on once the pi
# has booted on and the ping_led turns on if there is an external
# wifi connection

import RPi.GPIO as GPIO
import time

startup_led = 11
ping_led = 13

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(startup_led, GPIO.OUT)
GPIO.setup(ping_led, GPIO.OUT)

GPIO.output(startup_led, GPIO.LOW)
GPIO.output(ping_led, GPIO.LOW)

for i in range(1):
    GPIO.output(startup_led, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(startup_led, GPIO.LOW)
    time.sleep(0.2)

print("Exited for-loop")

print("About to start the ping test: ")
import os
hostname = "apple.com"
response = os.system("ping -c 1 " + hostname)

while True:
    response = os.system("ping -c 1 " + hostname)
    GPIO.output(startup_led, GPIO.HIGH)
    if response == 0:
        print(hostname, 'is up!')
        GPIO.output(ping_led, GPIO.HIGH)
    else:
        print(hostname, 'is down!')
        GPIO.output(ping_led, GPIO.LOW)
    time.sleep(0.1)

GPIO.cleanup()