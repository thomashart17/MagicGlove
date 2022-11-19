from camera_detect import *
from colour_detect import *
from range_sensor import *
from MagicGlove.gcp_text2speech import *

def main():
    # var for gcp
    audio_file = "/home/magicglove/MagicGlove/test/audiofile.mp3"

    # if COLOUR BUTTON clicked:
    gcp_phrase = "Colour Detection ON"
    speech_to_text(gcp_phrase, audio_file)
    call_colour_detection()

    # if OBSTACLE BUTTON clicked:
    # gcp_phrase = "Spatial Recognition ON"
    # speech_to_text(gcp_phrase, audio_file)
    # call_range_sensor()

    # if LIGHT DETECTION BUTTON clicked:
    # gcp_phrase = "Light Detection ON"
    # speech_to_text(gcp_phrase, audio_file)
    # call_light_detection()

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

    # call light detector file
    # returns true or false store value in lights_on, example code:

    lights_on = True # true = lights on, true = lights off
    if lights_on == True:
        gcp_phrase = "The lights are on"
        speech_to_text(gcp_phrase, audio_file)
    else:
        gcp_phrase = "The lights are on"
        speech_to_text(gcp_phrase, audio_file)




if __name__ == "__main__":
    main()
