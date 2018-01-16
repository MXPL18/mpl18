import pandas
import matplotlib.pyplot as plt
import datetime

unrate=pandas.read_csv("UNRATE.csv")
print(type(unrate))


first_twelve=unrate[0:12]
xaxis=first_twelve['DATE']
data=first_twelve['UNRATE']
print(xaxis)
print(data)

date_time=pandas.to_datetime(xaxis)

plt.plot(date_time,first_twelve['UNRATE'])

plt.xticks(rotation=90)
plt.show()
