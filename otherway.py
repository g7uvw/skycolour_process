import csv
import datetime

data = []

with open("smalldata.csv") as f:
    reader = csv.reader(f, delimiter=',')

    prev_date = None

    for row in reader:

        date = datetime.datetime.strptime(row[0], "%Y-%mm-%dd %H:%M:%S")

        if prev_date:
            diff = date - prev_date

            if diff > datetime.timedelta(minutes=1):

                for i in range((int(diff.total_seconds() / 60) - 1)):
                    new_date = prev_date + datetime.timedelta(minutes=i + 1)
                    new_row = [str(new_date)] + row[1:]

                    data.append(",".join(new_row))

        prev_date = date

        data.append(",".join(row))

print(data)
