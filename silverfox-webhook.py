import json
from multiprocessing import pool
import re
from tkinter.tix import Tree
import requests
import pyautogui
import time

# Webhook url for slack intergration.
webhook_url = 'https://hooks.slack.com/workflows/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'

# Using requests library to push http post to slack url. 
# Data can be anything that you would like to to be. 
# Be sure to change the variables on the slack channel config. 😉
data = { 'Detection': 'MC33 dectected passing the security desk!' }
post_to_slack = requests.post(webhook_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})

# Code for hook execution. Will detect if alarm is sounded. 
while 1:
    if pyautogui.locateOnScreen('target.png') != None:
        print("I can see it!")
        time.sleep(5)
    else:
        print("I can't see shit!")
        time.sleep(5)


# while True:
#     find_value = pyautogui.locateOnScreen('target.png')
#     if find_value == None:
#         pass
#     else:
#         post_to_slack
#     find_value
