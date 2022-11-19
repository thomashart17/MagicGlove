import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
delayt = .1 
value = 0 # this variable will be used to store the ldr value
ldr = 7 #ldr is connected with pin number 7
#led = 11 #led is connected with pin number 11
GPIO.setup(led, GPIO.OUT) # as led is an output device so that’s why we set it to output.
GPIO.output(led, False) # keep led off by default 
def rc_time (ldr):
    count = 0

    #Output on the pin for
    GPIO.setup(ldr, GPIO.OUT)
    GPIO.output(ldr, GPIO.LOW)
    time.sleep(delayt)

    #Change the pin back to input
    GPIO.setup(ldr, GPIO.IN)

    #Count until the pin goes high
    while (GPIO.input(ldr) == 0):
        count += 1

    return count


#Catch when script is interrupted, cleanup correctly
try:
    #light = True when it's light and False when dark
    while True:
        value = rc_time(ldr)
        if (value <= 200):
                light = True
                #GPIO.output(led, GPIO.LOW) # for the led
        if (value > 200):
                light = False
                #GPIO.output(led, GPIO.HIGH) #for the led
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
