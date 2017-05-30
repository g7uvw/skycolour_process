import csv
import datetime
import numpy as np
import scipy.misc as smp
from scipy.misc import imsave
import math

# Create a 1024x1024x3 array of 8 bit unsigned integers
data = np.zeros( (200,1440,3), dtype=np.uint8 )
#2016-12-27 15:08:38
with open("minutedata.csv", 'rb') as f:
    reader = csv.reader(f, delimiter=',')
    divisor = 1#8
    pixelcount = 0
    imagerow = 0
    for row in reader:
        date = datetime.datetime.strptime (row [0],"%Y-%m-%d %H:%M:%S")
        red = int(row[1])
        green = int(row[2])
        blue = int(row[3])
        clear = int(row[4])
        lux = int(row[5])
        divisor = 1
        if red or blue or green > 14000:
            divisor = 8 #60
        else:
            if red or blue or green > 3000:
                divisor = 4#16

        red = red / divisor
        green = green / divisor
        blue = blue / divisor
        if pixelcount > 1439:
            pixelcount = 0
            imagerow +=1
        data[imagerow,pixelcount] = [red,green,blue]
        RGB = (red * 65536) + (green * 256) + blue
        print pixelcount, imagerow
        pixelcount+=1

        #print date, hex(RGB)
    img = smp.toimage( data )       # Create a PIL image
    img.show()                      # View in default viewer
    imsave('sky.png',data)
