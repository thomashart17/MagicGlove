import RPi.GPIO as GPIO

def button_power_callback():
    print("Power Button was pushed!")

def button_feature_callback():
    print("Feature Button was pushed!")

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

BUTTON_POWER = 10
BUTTON_FEATURE = 9

#Pin 9 & 10 is input pin and set intial value to be pulled low (off)
GPIO.setup(BUTTON_POWER, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(BUTTON_FEATURE, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#attach event to pin
GPIO.add_event_detect(BUTTON_POWER, GPIO.RISING, callback=button_power_callback)
GPIO.add_event_detect(BUTTON_FEATURE, GPIO.RISING, callback=button_feature_callback)

message = input("Press enter to quit\n\n")
GPIO.cleanup()