import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

def light_intensity():
    count = 0
    ldr = 7 #ldr is connected with pin number 7
    count = 0
    delayt = 0.1

    #Output on the pin for
    GPIO.setup(ldr, GPIO.OUT)
    GPIO.output(ldr, GPIO.LOW)
    time.sleep(delayt)
    GPIO.setup(ldr, GPIO.IN)

    time.sleep(0.1)

    #Change the pin back to input
    GPIO.setup(7, GPIO.IN)
  
    #Count until the pin goes high
    while (GPIO.input(ldr) == 0):
        count += 1

    return count

if __name__ == "__main__":
    try:
        # Main loop
        while True:
            print(light_intensity())
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()
