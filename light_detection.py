import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

resistor_pin = 7

while True: #def rc_time(pin):
    GPIO.setup(resistor_pin, GPIO.OUT)
    GPIO.output(resistor_pin, GPIO.LOW)
    time.sleep(0.1)

    GPIO.setup(resistor_pin, GPIO.IN) # this is now reading values from the pin

    current_time = time.time()
    difference = 0

    while GPIO.input(resistor_pin) == GPIO.LOW:
        difference = time.time() - current_time #check if the voltage value from the pin reached teh high value (the "on" state)
        #now the diff value gives the time it took for the capacitor to be charged up
        #time it takes for the capacitor to charge is higher when the capacitance is higher
        #the longer it takes the higher ressitance in the photo resistor - the R goes doesn when light increases

        print(difference * 1000)
        time.sleep(1)
