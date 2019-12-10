#!/usr/bin/python3
# Apply regex pattern in Feed-v2  function

import feedparser
import subprocess
import os
import re
from datetime import date
from dateutil import parser
import wget

# Script for DigiKam
feed2 = feedparser.parse("https://www.digikam.org/index.xml")
v2 = (feed2.entries[0]['title'][:-12]).split()[-1]
if v2 == 'Reci' or v2 =='Pr':
    v2 = (feed2.entries[1]['title'][:-12]).split()[-1]

def check_file():
    if os.path.isfile('/opt/appimage/digikam.appimage'):
        return True
    else:
        return False

def version():
    global ver
    p = subprocess.Popen(["/opt/appimage/digikam.appimage", "-v"], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, shell=False)
    f2,err = p.communicate()
    ver = (f2.split()[-1]).decode('ascii')
    print('Digikam version:', ver)
    #return ver

def downloader(v2):
    # Obtain new URL
    url = "https://download.kde.org/stable/digikam/X/digikam-X-x86-64.appimage"
    url2 = url.replace("X",v2)
    print("Downloading: ", url2)
    # Download the file:
    wget.download(url2, "/tmp/digikam.appimage")
    os.popen("sudo mv digikam.appimage /opt/appimage/")
    os.popen("sudo chmod 775 /opt/appimage/digikam.appimage")
    # Check Version
    version()
    if ver == v2:
        print("File downloaded: ", ver, v2)

if check_file():
    version()
    # print(v1,v2)
    if ver == v2:
        print("DigiKam: Up-to-date")
    else:
        print("DigiKam: ", v2, "is available!")

        downloader(v2)
else:
    print('Digikam not installed, Downloading..')
    downloader(v2)

print('Done..')
