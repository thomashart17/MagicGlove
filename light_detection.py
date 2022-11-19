import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

resistor_pin = 7


def resistor_time(resistor_pin):
    reading = 0 #storing the detector value
    GPIO.setup(resistor_pin, GPIO.OUT)
    GPIO.output(resistor_pin, GPIO.LOW)
    time.sleep(0.1)
    
    GPIO.setup(pin, GPIO.IN) #reversing pin back to input
    
    while (GPIO.input(pin) == GPIO.LOW):
        reading +=1
      
    return reading