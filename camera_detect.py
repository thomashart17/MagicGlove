from picamera2 import Picamera2
from time import sleep
from colour_detect import *

# if button pressed called this function

def image_capture(path):

    camera = Picamera2()
    sleep(2)
    camera.start()
    camera.capture_file(path)
    print("FILE CAPTURED")
    sleep(2)
    colour_detect_on_image(path)


if __name__ == "__main__":
    image_capture("test")
