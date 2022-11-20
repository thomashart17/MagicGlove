from camera_detect import *
from colour_detect import *
from range_sensor import *
from gcp_text2speech import *
from light_detection import *
import RPi.GPIO as GPIO
import time

def main():
    # var for gcp
    audio_file = "/home/magicglove/MagicGlove/test/audiofile.mp3"
    image_file = "/home/magicglove/MagicGlove/test/image.jpg"

    # interfacing gpio
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)

    BUTTON_POWER = 10
    BUTTON_COLOR_DETECT = 9
    BUTTON_SPATIAL_REC = 11
    BUTTON_LIGHT_INTENSE = 0

    #Pin 9,10,11 & 0 is input pin and set intial value to be pulled low (off)
    GPIO.setup(BUTTON_POWER, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(BUTTON_COLOR_DETECT, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(BUTTON_SPATIAL_REC, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(BUTTON_LIGHT_INTENSE, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    # Main Loop for the Device
    while (True):
        print("Device started")
        # intalize
        power = False
        colorStatus = False
        spatialStatus = False
        lightStatus = False

        def callback():
            print("in callback")
            power = True

        GPIO.add_event_detect(BUTTON_POWER, GPIO.FALLING, callback=callback)
        while (True):
            # Wait for power to turn on
            if (power): break
        print("power")
        GPIO.remove_event_detect(BUTTON_POWER)
        GPIO.add_event_detect(BUTTON_POWER, GPIO.FALLING, callback=lambda pin: (power := False))

        while (power):
            print("Power On")

            #attach event to pin
            GPIO.add_event_detect(BUTTON_COLOR_DETECT, GPIO.FALLING, callback=lambda pin: (colorStatus := True))
            GPIO.add_event_detect(BUTTON_SPATIAL_REC, GPIO.FALLING, callback=lambda pin: (spatialStatus := True))
            GPIO.add_event_detect(BUTTON_LIGHT_INTENSE, GPIO.FALLING, callback=lambda pin: (lightStatus := True))

            while (True):
                # Wait for button press
                if ((not power) or colorStatus or spatialStatus or lightStatus): break

            GPIO.remove_event_detect(BUTTON_COLOR_DETECT)
            GPIO.remove_event_detect(BUTTON_SPATIAL_REC)
            GPIO.remove_event_detect(BUTTON_LIGHT_INTENSE)

            if (not power):
                break
            elif (colorStatus):
                speech_to_text("Colour detection on", audio_file)

                # get image
                image_capture(image_file)

                # run colour detect on image and get colour
                recent_colour = colour_detect_on_image(image_file)
                print(recent_colour)

                colorStatus = False

                # call gcp
                speech_to_text(f"The colour is {recent_colour}", audio_file)
            elif (spatialStatus):
                speech_to_text("Spatial recognition on.", audio_file)
                call_range_sensor()

                spatialStatus = False
            else:
                speech_to_text("Light detection on", audio_file)
                
                if light_intensity():
                    speech_to_text("The lights are on", audio_file)
                else:
                    speech_to_text("The lights are off", audio_file)

                lightStatus = False
        print("Power Off")

if __name__ == "__main__":
    main()
