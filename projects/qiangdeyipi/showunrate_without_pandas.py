import pandas
import matplotlib.pyplot as plt
import datetime

f = open('UNRATE.csv', 'r')
data = f.read()
rows = data.split('\n')
unrate=[]
for row in rows:
    song=row.split(',')
    unrate.append(song)
print(unrate)


xaxis=["2017/1/1","2017/2/1","2017/3/1","2017/4/1","2017/5/1","2017/6/1","2017/7/1","2017/8/1","2017/9/1","2017/10/1","2017/11/1","2017/12/1"]
data=[1,3,5,7,3,1,2,5,10,9,11,62]


date_time=[]
for xax in xaxis:
    date = datetime.datetime.strptime(xax,'%Y/%m/%d')
    date_time.append(date)

plt.plot(date_time,data)

plt.xticks(rotation=90)
plt.show()
