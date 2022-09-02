import json
from multiprocessing import pool
import re
from tkinter.tix import Tree
from cv2 import VideoCapture, imshow, imwrite
import requests
import pyautogui
import time
import cv2

# Webhook url for slack intergration.
webhook_url = 'https://hooks.slack.com/workflows/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'

# Using requests library to push http post to slack url. 
# Data can be anything that you would like to to be. 
# Be sure to change the variables on the slack channel config. 😉
data = { 'Detection': 'MC33 dectected passing the security desk!' }

# post_to_slack = requests.post(webhook_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})

# Minimize window after script execute.
pyautogui.hotkey("win", 'down')

# Setting up camera functionality.
# Will display a still image of the last person walking out with scanner device. 
cam_port = 1
cam = VideoCapture(cam_port)
result, image = cam.read()

# Code for hook execution. Will detect if alarm is sounded. 
while 1:
    if pyautogui.locateOnScreen('target.png') != None:
        print("I can see it!")
        # requests.post(webhook_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
        if result:
            imshow('PersonCapture', image)
            imwrite('PersonCapture.png', image)
        time.sleep(5)
    else:
        print("Nope,I can't see it!")
        time.sleep(1)