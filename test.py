import pandas as pd
import io
import datetime
import numpy as np
import scipy.misc as smp
from scipy.misc import imsave
import math

data = np.zeros( (100,1440,3), dtype=np.uint8 )
z = pd.read_csv('minutedata_big.csv')
#z = pd.read_csv('minutedata_big.csv')
z = z[~z.time.duplicated()]
#z = z[~z.time.duplicated()]
z['time'] = pd.to_datetime(z['time'])

#z['time'] = pd.to_datetime(z['time'])
z.set_index('time').reindex(pd.date_range(min(z['time']), max(z['time']), freq="1min"))
z.ffill()



#z['time'] = pd.to_datetime(z['time'])

#z = z.set_index('time').reindex(pd.date_range(min(z['time']), max(z['time']), freq="1min")).ffill()

#z = z.ffill()

divisor = 1#1#8
pixelcount = 0
imagerow = 0
for index,row in z.iterrows():
    red = int(row[1])
    green = int(row[2])
    blue = int(row[3])
    clear = int(row[4])
    lux = int(row[5])
    divisor = 1
    if pixelcount > 1439:
        pixelcount = 0
        imagerow +=2
    data[imagerow,pixelcount] = [red,green,blue]
    data[imagerow+1,pixelcount] = [red,green,blue]
    RGB = (red * 65536) + (green * 256) + blue
    pixelcount += 1
img = smp.toimage( data )       # Create a PIL image
img.show()                      # View in default viewer
imsave('test.png',data)
