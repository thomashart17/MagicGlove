import RPi.GPIO as GPIO
import time

def light_intensity ():
    
    light_on = False
    count = 0
    delayt = .1 
    ldr = 7 #ldr is connected with pin number 7

    GPIO.setup(ldr, GPIO.OUT)
    GPIO.output(ldr, GPIO.LOW)
    time.sleep(delayt)

    #Change the pin back to input
    GPIO.setup(ldr, GPIO.IN)

    #Count until the pin goes high
    while (GPIO.input(ldr) == GPIO.LOW):
        count += 1

    if (count <= 200):
        light_on = True
    else:
        light_on = False

    return light_on

