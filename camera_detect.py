from picamera import PiCamera
from time import sleep

# if button prested called this function

def image_capture():
    image_path = "/pi/recent_image.jpg"
    
    camera = PiCamera()
    camera.start_preview(alpha=192)
    sleep(1)
    camera.capture(image_path)
    camera.stop_preview()

    return image_path