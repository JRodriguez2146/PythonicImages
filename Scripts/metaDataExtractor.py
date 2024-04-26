import os
from PIL import Image
from PIL.ExifTags import TAGS

img_file = r" **add image path here** "

image = Image.open(img_file)

exif = {}
for tag, value in image.getexif().items():
    if tag in TAGS:
        exif[TAGS[tag]] = value

print(exif)

if "GPSInfo" in exif:
    geo_coordinate = '{0} {1} {2:.2f} {3}, {4} {5} {6:.2f} {7}'.format(
        exif["GPSInfo"][2][0][0],
        exif["GPSInfo"][2][0][0],
        exif["GPSInfo"][2][0][0] / exif["GPSInfo"][2][2][1],
        exif["GPSInfo"][1],
        exif["GPSInfo"][4][0][0],
        exif["GPSInfo"][4][0][0],
        exif["GPSInfo"][4][0][0] / exif["GPSInfo"][2][2][1],
        exif["GPSInfo"][3] )
    
    print(geo_coordinate)
        