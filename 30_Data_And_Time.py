import datetime as dt
import arrow

today = (dt.datetime.today())
print(today.time())
print(today.date())

now = arrow.now()
print("Date:", now.format('DD-MM-YYYY'))
print("Time:", now.format('HH:mm:ss'))
print("Time:", now.format('HH:mm:ss:ms'))
