from camera_detect import *
from colour_detect import *
from range_sensor import *
from gcp_text2speech import *
from light_detection import *
<<<<<<< HEAD
from gcp_text2speech import *
=======
>>>>>>> 242c2fb54d083ea8434b777acda7beeb4153005a
import RPi.GPIO as GPIO
import time

def main():

    # time lag for buttons
    def last_button_press_calculate():
        global last_button_press
        if time.time() - last_button_press >= 0.3:
            last_button_press = time.time()

    # power button check
    def button_power_callback(pin):
        last_button_press_calculate()
        print("Power Button was pushed!")
        power =  not power

    if power == True:
        def button_color_callback(pin):
            last_button_press_calculate()
            # features
            gcp_phrase = "Colour Detection ON"
            speech_to_text(gcp_phrase, audio_file)
            call_colour_detection()

        def button_spatial_callback(pin):
            last_button_press_calculate()
            #features
            gcp_phrase = "Spatial Recognition ON"
            speech_to_text(gcp_phrase, audio_file)
            call_range_sensor()

        def button_light_intense_callback(pin):
            last_button_press_calculate()
            #features
            gcp_phrase = "Light Detection ON"
            speech_to_text(gcp_phrase, audio_file)
            call_light_detection()


    def call_colour_detection():
        image_path = "/home/magicglove/MagicGlove/test/image.jpg"

        # get image
        image_capture(image_path)

        # run colour detect on image and get colour
        recent_colour = colour_detect_on_image(image_path)
        print(recent_colour)
        colour_phrase = f"The colour is {recent_colour}"

        # call gcp
        audio_file = "/home/magicglove/MagicGlove/test/audiofile.mp3"
        speech_to_text(colour_phrase, audio_file)

    def call_light_detection():
        # var for gcp
        audio_file = "/home/magicglove/MagicGlove/test/audiofile.mp3"

        # call light detector file to get bool value
        lights_on = light_intensity()
        
        if lights_on == True:
            gcp_phrase = "The lights are on"
            speech_to_text(gcp_phrase, audio_file)
        else:
            gcp_phrase = "The lights are on"
            speech_to_text(gcp_phrase, audio_file)

    ##################################################################################################

    # var for gcp
    audio_file = "/home/magicglove/MagicGlove/test/audiofile.mp3"

    # intalize
    power = False

    # interfacing gpio
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


if __name__ == "__main__":
    main()
