import RPi.GPIO as GPIO
import time

def light_intensity():
    #GPIO.setmode(GPIO.BOARD)

    resistorPin = 7

    while True:
        GPIO.setup(resistorPin, GPIO.OUT)
        GPIO.output(resistorPin, GPIO.LOW)
        time.sleep(0.1)
        
        GPIO.setup(resistorPin, GPIO.IN)
        currentTime = time.time()
        diff = 0
        
        while(GPIO.input(resistorPin) == GPIO.LOW):
            diff  = time.time() - currentTime
            print(diff)

        out = (diff * 1000)
        print(out)

        light_on = out <= 50

        return light_on
            
