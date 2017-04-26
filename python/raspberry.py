import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)  # set board mode to Broadcom

GPIO.setup(17, GPIO.OUT)  # set up pin 17
GPIO.setup(18, GPIO.OUT)  # set up pin 18

GPIO.output(17, 1)  # turn on pin 17
GPIO.output(18, 0)  # turn off pin 18

# Desfazendo as modificações do GPIO
gpio.cleanup()
