import json
import requests
import pyautogui

# Webhook url for slack intergration.
webhook_url = 'https://hooks.slack.com/workflows/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'
# Search the page for he needed item/button.
data = { 'Detection': 'MC33 dectected passing the security desk!' }
requests.post(webhook_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})