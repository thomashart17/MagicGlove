import RPi.GPIO as GPIO
import time

last_button_press = 0

def last_button_press_calculate():
    global last_button_press
    if time.time() - last_button_press >= 0.3:
        last_button_press = time.time()

def button_power_callback(pin):
    last_button_press_calculate()
    print("Power Button was pushed!")

def button_color_callback(pin):
   last_button_press_calculate()
   print("Color detection Button was pushed!")

def button_spatial_callback(pin):
    last_button_press_calculate()
    print("Spatial button was pushed!")

def button_light_intense_callback(pin):
    last_button_press_calculate()
    print("light intense was pushed!")

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

BUTTON_POWER = 10
BUTTON_COLOR_DETECT = 9
BUTTON_SPATIAL_REC = 11
BUTTON_LIGHT_INTENSE = 0

#Pin 9,10,11 & 0 is input pin and set intial value to be pulled low (off)
GPIO.setup(BUTTON_POWER, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(BUTTON_COLOR_DETECT, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(BUTTON_SPATIAL_REC, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(BUTTON_LIGHT_INTENSE, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#attach event to pin
GPIO.add_event_detect(BUTTON_POWER, GPIO.FALLING, callback=button_power_callback)
GPIO.add_event_detect(BUTTON_COLOR_DETECT, GPIO.FALLING, callback= button_color_callback)
GPIO.add_event_detect(BUTTON_SPATIAL_REC, GPIO.FALLING, callback=button_spatial_callback)
GPIO.add_event_detect(BUTTON_LIGHT_INTENSE, GPIO.FALLING, callback=button_light_intense_callback)

message = input("Press enter to quit\n\n")
GPIO.cleanup()
