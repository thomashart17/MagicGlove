from camera_detect import *
#from colour_detect import *

def main():
    # if button clicked:
    try:
        image_capture()
    except:
        print("CAM FAILURE")

    #colour_detect()


if __name__ == "__main__":
    main()