import pandas as pd
z = pd.read_csv('minutedata.csv')
for w in z.time.duplicated():

    if w:
        print z
