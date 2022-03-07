import RPi.GPIO as GPIO
import time
import os


def shutdown(channel):
    os.system('sudo shutdown -h now')
    pass


def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(5, GPIO.FALLING, callback=shutdown, bouncetime=2000)


def loop():
    while True:
        time.sleep(1)


if __name__ == '__main__':
    setup()
    loop()
