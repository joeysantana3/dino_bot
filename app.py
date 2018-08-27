from PIL import ImageGrab, ImageOps, Image
import pyautogui
import time
from numpy import *
import random

# While game browser windows is maximized
# www.trex-game.skipser.com
# First coord, lower = to left
# Second coord, lower = up

class Coordintates():
    replayButton = (1250, 410)
    dino_loc = (1035, 415)


def restart_game():
    pyautogui.click(Coordintates.replayButton)
    pyautogui.click(Coordintates.replayButton)


def press_space():
    pyautogui.keyDown('space')
    time.sleep(.05)
    print('Jump')
    pyautogui.keyUp('space')


number = 1


def box_image_check():
    global number
    box = (Coordintates.dino_loc[0]+1800, Coordintates.dino_loc[1]+400, Coordintates.dino_loc[0]+120+2000, Coordintates.dino_loc[1]+500)
    image = ImageGrab.grab(box)
    image.save("{}test.png".format(number))
    number += 1


def pixel_check():
    box = (Coordintates.dino_loc[0]+1800 , Coordintates.dino_loc[1]+400, Coordintates.dino_loc[0]+120+2000, Coordintates.dino_loc[1]+500)
    image = ImageGrab.grab(box)
    image.save("test.png")
    grayimage = ImageOps.grayscale(image)
    a = array(grayimage.getcolors())
    print(a.sum())
    return a.sum()


def test_location():
    pyautogui.click(Coordintates.dino_loc)

# def test_box():
#     # box = (Coordintates.dino_loc[0]+50, Coordintates.dino_loc[1], Coordintates.dino_loc[0]+40, Coordintates.dino_loc[1]+30)
#     pyautogui.click(Coordintates.dino_loc[0]+120, Coordintates.dino_loc[1])
#     time.sleep(.5)
#     # pyautogui.click(Coordintates.dino_loc[0]+50, Coordintates.dino_loc[1])
#     # time.sleep(.5)
#     # pyautogui.click(Coordintates.dino_loc[0], Coordintates.dino_loc[1]+30)
#     # time.sleep(.5)
#     pyautogui.click(Coordintates.dino_loc[0]+120+50, Coordintates.dino_loc[1]+30)


def auto_jump():
    if 33100 <= pixel_check() <= 33200:
        pass
    else:
        time.sleep(.3)
        press_space()


restart_game()
while True:
    # pixel_check()
    auto_jump()
    # box_image_check()
# test_box()
# press_space()
# time.sleep(1)
# press_space()


