import random
from dateutil.parser import parse
from datetime import datetime

AVG_LATENCY= 0.03
SIGMA= 0.005

print("date, latency")
for i in range(0,60):
    for j in range(0,200):
        date = i + random.random()
        latency = random.gauss(AVG_LATENCY, SIGMA)
        print(",".join(map(str,[date,latency])))