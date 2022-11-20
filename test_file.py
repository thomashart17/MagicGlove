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
  
    #Count until the pin goes high
    while (GPIO.input(ldr) == GPIO.LOW):
        count += 1

    return count

def calling():
    timeout = 2 # [seconds]
    timeout_start = time.time()
    while (True and time.time() < timeout_start + timeout):
            store = light_intensity()
            print(store)
    
    if ( store <= 200 ):
            print("Lights are ON")
    else:
        print("Lights are OFF")
    

if __name__ == "__main__":
    calling()