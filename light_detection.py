import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

delayt = .1 
ldr = 7 #ldr is connected with pin number 7

def light_intensity ():
    intensity = 0

    #Output on the pin for
    GPIO.setup(ldr, GPIO.OUT)
    GPIO.output(ldr, GPIO.LOW)
    time.sleep(delayt)

    #Change the pin back to input
    GPIO.setup(ldr, GPIO.IN)

    #Count until the pin goes high
    while (GPIO.input(ldr) == GPIO.LOW):
        intensity += 1

    return intensity
