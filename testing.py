import datetime
import numpy as np
import scipy.misc as smp
from scipy.misc import imsave
import math
import pandas as pd
import io

# Create a 100x1440x3 array of 8 bit unsigned integers
data = np.zeros( (200,1440,3), dtype=np.uint8 )


z = pd.read_csv('minutedata3.csv')
z = z[~z.time.duplicated()]
z['time'] = pd.to_datetime(z['time'])

z = z.set_index('time')
z = z.asfreq('min', 'nearest')

divisor = 1#1#8
pixelcount = 0
imagerow = 0
for index,row in z.iterrows():
    #date = datetime.datetime.strptime (row [0],"%Y-%m-%d %H:%M:%S")
    red = int(row[1])
    green = int(row[2])
    blue = int(row[3])
    clear = int(row[4])
    #lux = int(row[5])
    divisor = 1
    if red or blue or green > 14000:
        divisor = 8 # 8 #60
    else:
        if red or blue or green > 3000:
            divisor = 4 #4#16
    red = red / divisor
    if red > 255:
        red = 255
    green = green / divisor
    if green > 255:
        green = 255
    blue = blue / divisor
    if blue > 255:
        blue = 255
    if pixelcount > 1439:
        pixelcount = 0
        imagerow +=2
    data[imagerow,pixelcount] = [red,green,blue]
    data[imagerow+1,pixelcount] = [red,green,blue]
    RGB = (red * 65536) + (green * 256) + blue
    #print pixelcount, imagerow
    pixelcount += 1
    #print date, hex(RGB)
img = smp.toimage( data )       # Create a PIL image
img.show()                      # View in default viewer
imsave('sky.png',data)
