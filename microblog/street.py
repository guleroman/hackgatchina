import os
#!/usr/bin/env python3
import re
import urllib.request
import random
import sys
import csv

# Create a route from:
# https://www.plotaroute.com/routeplanner

GPX_FILE = open('22.gpx').read()

API_KEY = "&key=" + "AIzaSyCLXxaOd3K8TmDd21PYtP8nK_ibDZ4h8Ss"
SAVE_PATH = 'C:\\Users\\user\\Desktop\\HACK_GATCHINA\\22'
SIZE = "1600x800"   # currently limited to 600x600.
# Grab all of the "trkpt" elements
def getStreet(address, save_path, num):
    base = "https://maps.googleapis.com/maps/api/streetview?size=" + SIZE

    location = "&location=" + address
    heading = "&heading=" + '0'#str(random.randint(0, 360))  # random horizontal angle
    url = base + location + heading + API_KEY

    file_name = "img_" + str(num)+".jpg"
    urllib.request.urlretrieve(url, os.path.join(save_path, file_name))

# parse gpx file for coordinates
matches = re.findall('<trkpt lat="([-0-9\.]+)" lon="([-0-9\.]+)">', GPX_FILE)

# create array of coordinates
coordinates = [lat + ',' + lon for lat, lon in matches]

# ==========================================================================================================
print (matches[0][0])
print('Running script ...')

start = 0
amount = len(coordinates)
with open('22.csv', mode='w') as wr_file:
    for i in range(start, amount):
        getStreet(coordinates[i], SAVE_PATH, str(i))
        sys.stdout.write("\r" + "[" + str(i) + " / " + str(amount - 1) + "] " + "Location: " + coordinates[i])
        sys.stdout.flush()

        wr_writer = csv.writer(wr_file, delimiter=',',  quoting=csv.QUOTE_MINIMAL)

        wr_writer.writerow([str(i), matches[i][0], matches[i][1]])


print('\n Script completed ...')
