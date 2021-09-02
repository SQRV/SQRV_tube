# warna
#git clone https://github.com/SQRV/SQRV_tube.git
h="\033[32;1m"

# module
import pytube
import os,sys,time,requests
from time import sleep
# tampilan
os.system("clear")
sleep(1)
os.system("toilet -f future sqrv tube | lolcat")
sleep(1)
banner= h+"""
[•]───────────────────────────────────────────[•]
          You can download the video
             easily from SQRV Tube
[•]───────────────────────────────────────────[•]  """
print(banner)
sleep(1)
print('Download video from Youtube')
sleep(1)
url = input ('Enter video url : ')
sleep(1)
print('loading...')
pytube.YouTube(url).streams.get_highest_resolution().download('/sdcard/SQEV_tube')
print('Done')

