import RPi.GPIO as GPIO
import time

last_button_press = 0

def button_power_callback(pin):
    global last_button_press
    if time.time() - last_button_press >= 0.3:
        last_button_press = time.time()
        print("Power Button was pushed!")

def button_feature_callback(pin):
    global last_button_press
    if time.time() - last_button_press >= 0.3:
        last_button_press = time.time()
        print("Feature Button was pushed!")

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

BUTTON_POWER = 10
BUTTON_FEATURE = 9

#Pin 9 & 10 is input pin and set intial value to be pulled low (off)
GPIO.setup(BUTTON_POWER, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(BUTTON_FEATURE, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#attach event to pin
GPIO.add_event_detect(BUTTON_POWER, GPIO.FALLING, callback=button_power_callback)
GPIO.add_event_detect(BUTTON_FEATURE, GPIO.FALLING, callback=button_feature_callback)

message = input("Press enter to quit\n\n")
GPIO.cleanup()
