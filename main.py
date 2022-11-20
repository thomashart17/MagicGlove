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
    GPIO.setmode(GPIO.BCM)

    BUTTON_POWER = 10
    BUTTON_COLOR_DETECT = 9
    BUTTON_SPATIAL_REC = 11
    BUTTON_LIGHT_INTENSE = 0

    #Pin 9,10,11 & 0 is input pin and set intial value to be pulled low (off)
    GPIO.setup(BUTTON_POWER, GPIO.IN)
    GPIO.setup(BUTTON_COLOR_DETECT, GPIO.IN)
    GPIO.setup(BUTTON_SPATIAL_REC, GPIO.IN)
    GPIO.setup(BUTTON_LIGHT_INTENSE, GPIO.IN)

    # Main Loop for the Device
    while (True):
        print("Device started")
        # intalize
        power = False
        colorStatus = False
        spatialStatus = False
        lightStatus = False

        while (GPIO.input(BUTTON_POWER) != GPIO.HIGH): pass
        while (GPIO.input(BUTTON_POWER) != GPIO.LOW): pass
        power = True
        print("power")

        while (power):
            print("Power On")

            while ((GPIO.input(BUTTON_POWER) != GPIO.HIGH) and (GPIO.input(BUTTON_COLOR_DETECT) != GPIO.HIGH) and (GPIO.input(BUTTON_SPATIAL_REC) != GPIO.HIGH) and (GPIO.input(BUTTON_LIGHT_INTENSE) != GPIO.HIGH)):
                if (GPIO.input(BUTTON_POWER) == GPIO.HIGH):
                    print("POWER")
                    while (GPIO.input(BUTTON_POWER) == GPIO.HIGH): pass
                    power = False
                    break
                elif (GPIO.input(BUTTON_COLOR_DETECT) == GPIO.HIGH):
                    print("COLOR")
                    while (GPIO.input(BUTTON_COLOR_DETECT) == GPIO.HIGH): pass
                    colorStatus = True
                    break
                elif (GPIO.input(BUTTON_SPATIAL_REC) == GPIO.HIGH):
                    print("SPATIAL")
                    while (GPIO.input(BUTTON_SPATIAL_REC) == GPIO.HIGH): pass
                    spatialStatus = True
                    break
                elif (GPIO.input(BUTTON_LIGHT_INTENSE) == GPIO.HIGH):
                    print("LIGHT")
                    while (GPIO.input(BUTTON_LIGHT_INTENSE) == GPIO.HIGH): pass
                    lightStatus = True
                    break

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
            elif (lightStatus):
                print('Entered the light thread')
                speech_to_text("Light detection on", audio_file)

                intensity = light_intensity()
                print('Status for light intensity: ', intensity)

                if intensity:
                    print(intensity)
                    print('start')
                    speech_to_text("The lights are on", audio_file)
                else:
                    speech_to_text("The lights are off", audio_file)
                    

                lightStatus = False
        print("Power Off")

if __name__ == "__main__":
    main()
