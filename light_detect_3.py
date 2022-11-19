import RPi.GPIU
import time

GPIO.setmode(GPIO.BOARD)

resistor_pin = 7

def photoresistor(resistor_pin):
    count = 0

    GPIO.setup(resistor_pin, GPIO.OUT) #setting the pin to the output mode to write values 
    GPIO.output(resistor_pin, GPIO.LOW) #writing a low voltage value to the pin "turnong it off"
    time.sleep(0.1)

    GPIO.setup(pin_to_circuit, GPIO.IN) #start reading

    while (GPIO.input(resistor_pin) == GPIO.LOW): #stay in the loop until the pin gets to high
        count+=1

    return count

try:
    while true:
        print(photoresistor(resistor_pin))
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()

    #dark returns high and light returns low values
    
    
    