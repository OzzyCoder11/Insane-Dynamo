import platform # comments so you know there is no ;s
import subprocess#
from sys import exit#
#
disalloweduuids = [
  "4C4C4544-0056-3910-8043-B9C04F4E3933"
]#
#
if platform.system() == "Windows":#
        uuid = subprocess.check_output("wmic csproduct get uuid").decode().split('\n')[1].strip()#
elif platform.system() == "Linux":#
        uuid = subprocess.check_output('cat /sys/class/dmi/id/product_uuid', shell=True).decode().strip()#
#
if uuid in disalloweduuids:#
  print("Your UUID is not allowed                      ")#
  input()#
  exit()#
