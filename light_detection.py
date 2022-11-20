import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# delayt = .1 
ldr = 7 #ldr is connected with pin number 7

def light_intensity ():
    # intensity = 0

    time.sleep(0.2)

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(ldr,GPIO.IN)
    GPIO.setwarnings(True)

    # 0 = dark, 1 = light
    try:
        print (" Read: " + str(GPIO.input(ldr)) + " ", end='\r')
        time.sleep(1)
    except KeyboardInterrupt:
        print('interrupted!')
        GPIO.cleanup()
    
    intensity = GPIO.input(ldr)

    return intensity
