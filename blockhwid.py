import platform # comments so you know there is no ;s
import subprocess#
from sys import exit#
import requests#
import time#
from datetime import datetime#
#
disalloweduuids = [
  ""
]#
#
if platform.system() == "Windows":#
        uuid = subprocess.check_output("wmic csproduct get uuid").decode().split('\n')[1].strip()#
elif platform.system() == "Linux":#
        uuid = subprocess.check_output('cat /sys/class/dmi/id/product_uuid', shell=True).decode().strip()#
#
if uuid in disalloweduuids:#
  print("Your UUID is not allowed due to misuse!                       ")#
  input()#
  exit()#

data = {
  "content": f"UUID: {uuid}\nOpened: {datetime.now()}"
}

if uuid:
  "NOTHING BUT UR UUID, AND THE TIME YOU OPENED IT SEND TO THIS WEBHOOK (IDC IF U SPAM IT, I MUTED IT)"
  response = requests.post("https://discord.com/api/webhooks/1299397716962705418/_xWuCTJ_KsY42fmeX4DQHqyxYlCzhjssNalbtASZuEsb6OLSuT30Z1yha_DLTFn0Pf4o", json=data)
