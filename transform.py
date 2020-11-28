import fileinput
from dateutil.parser import parse
from datetime import datetime


start_date = parse("2010-01-01T00:00:00,00").timestamp()
for i,line in enumerate(fileinput.input()):
    line = line.strip().split(",")
    if i == 0:
        line[0] = "old_date"
        line.append("date,")
        print(",".join(map(str,line)))
    else:
        line.append(datetime.fromtimestamp(start_date + i).isoformat())
        print(",".join(map(str,line)))