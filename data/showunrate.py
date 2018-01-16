import pandas
import matplotlib.pyplot as plt
import datetime

#unrate=pandas.read_csv("UNRATE.csv")
#print(type(unrate))

#xaxis=["2017/1/1","2017/2/1","2017/3/1","2017/4/1","2017/5/1","2017/6/1","2017/7/1","2017/8/1","2017/9/1","2017/10/1","2017/11/1","2017/12/1"]
xaxis=["2017/1/1","2017/1/2","2017/1/3","2017/1/4","2017/1/5","2017/1/6","2017/1/7","2017/1/8","2017/1/9","2017/1/10","2017/1/11","2017/1/12"]
data=[1,3,5,7,3,1,2,5,10,9,11,62]

#first_twelve=unrate[0:12]
#xaxis=first_twelve['DATE']
#data=first_twelve['UNRATE']
#print(xaxis)
#print(data)

#date_time=[]
#for xax in xaxis:
#    date = datetime.datetime.strptime(xax,'%Y/%m/%d')
#    date_time.append(date)
#print(date_time)
#plt.plot(date_time,first_twelve['UNRATE'])
plt.plot(xaxis,data)
#plt.plot()
plt.xticks(rotation=90)
plt.show()
