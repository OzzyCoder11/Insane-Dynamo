import platform # comments so you know there is no ;s
import subprocess#
from sys import exit#
#
disalloweduuids = [
  ""
]#
#
if platform.system() == "Windows":#
        uuid = subprocess.check_output("wmic csproduct get uuid").decode().split('\n')[1].strip()# for some reason no comment can be added below, but you can check it
elif platform.system() == "Linux":
        uuid = subprocess.check_output('cat /sys/class/dmi/id/product_uuid', shell=True).decode().strip()#
#
if uuid in dissalloweduuids:#
  print("Your UUID is not allowed                      ")#
  input()#
  exit()#
