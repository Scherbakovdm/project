from datetime import datetime as dt
import sys

t_date = dt.strptime(sys.argv[1], "%B %d, %Y %I:%M %p")
print(t_date)
print("Hello")
print(t_date.strftime("%H:%M"))
