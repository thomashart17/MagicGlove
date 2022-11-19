from camera_detect import *
from colour_detect import *
from range_sensor import *
# from gcp_text2speech import *

def main():
    # if COLOUR BUTTON clicked:
    call_colour_detection()

    # if OBSTACLE BUTTON clicked:
    # call_range_sensor()


def call_colour_detection():
    image_path = "/home/magicglove/MagicGlove/test/image.jpg"

    # get image
    image_capture(image_path)

    # run colour detect on image and get colour
    recent_colour = colour_detect_on_image(image_path)
    print(recent_colour)

    # call gcp
    # speech_to_text(recent_colour)


if __name__ == "__main__":
    main()
