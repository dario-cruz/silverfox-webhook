import json
from multiprocessing import pool
import re
from tkinter.tix import Tree
from turtle import pos, title
from cv2 import VideoCapture, imshow, imwrite
import requests
import pyautogui
import time
import cv2
import wx

# Creating a class for the UI.
class SilverFoxUI(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="SilverFox Webook by Dariocru", size=(300, 200))
        panel = wx.Panel(self)

        foxMenuBar = wx.MenuBar()
        foxMenu = wx.Menu()
        foxMenuItem = foxMenu.Append(wx.ID_EXIT, "Quit", "Quit Application")
        foxMenuBar.Append(foxMenu, '&File')
        self.SetMenuBar(foxMenuBar)

        self.Bind(wx.EVT_MENU, self.OnQuit, foxMenuItem)

        self.text_ctrl = wx.TextCtrl(panel, pos=(5,5))
        my_btn = wx.Button(panel, label="Click Here for Nothing!", pos=(5,55))

        self.Center()
        self.Show()
    def OnQuit(self, e):
        self.Close()

if __name__ == '__main__':
    app = wx.App()
    frame = SilverFoxUI()
    app.MainLoop()


# Webhook url for slack intergration.
webhook_url = ""
# Using requests library to push http post to slack url. 
# Data can be anything that you would like to to be. 
# Be sure to change the variables on the slack channel config. 😉
data = { 'Detection': 'MC33 dectected passing the security desk!' }

# post_to_slack = requests.post(webhook_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})

# Minimize window after script execute.
pyautogui.hotkey("win", 'down')

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



# Setting up camera functionality.
# Will display a still image of the last person walking out with scanner device.
# Work in progress. Commenting out for now.  
# cam_port = 1
# cam = VideoCapture(cam_port)
# result, image = cam.read()
