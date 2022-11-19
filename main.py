from camera_detect import *
from colour_detect import *
from range_sensor import *
# from gcp_text2speech import *

def main():
    # if COLOUR BUTTON clicked:
    colour_detect()

    # if OBSTACLE BUTTON clicked:
    # call_range_sensor()


def colour_detect():
    # get image
    image_capture()

    # run colour detect on image and get colour
    recent_colour = colour_detect()

    print(recent_colour)

    # call gcp
    # speech_to_text(recent_colour)


if __name__ == "__main__":
    main()