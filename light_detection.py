import RPi.GPIO as GPIO
import time
#GPIO.setmode(GPIO.BOARD)

def light_intensity ():
    intensity = 0

    ldr = 7 #ldr is connected with pin number 7
    light_on = False
    count = 0
    delayt = 0.1

    #Output on the pin for
    GPIO.setup(ldr, GPIO.OUT)
    GPIO.output(ldr, GPIO.LOW)
    time.sleep(delayt)
    GPIO.setup(ldr, GPIO.IN)

    timeout = 5 # [seconds]
    timeout_start = time.time()
    #Count until the pin goes high
    while (GPIO.input(ldr) == GPIO.LOW) and (time.time() < timeout_start + timeout):
        count += 1
        print(count)
    
    if(count <= 200) : 
        light_on = True
    else:
        light_on = False

    return light_on
