from picamera2 import Picamera2
from time import sleep

# if button pressed called this function

def image_capture():
    image_path = "/home/magicglove/MagicGlove/image.jpg"

    camera = Picamera2()
    camera.start()
    camera.capture_file(image_path)

    return image_path

if __name__ == "__main__":
    image_capture()
