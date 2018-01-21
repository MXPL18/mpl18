import serial
import serial.tools.list_ports
import time

f = open('mysongs.csv', 'r')
data = f.read()
rows = data.split('\n')
#print(rows[0:5])

print("Hello1")

songs=[]
for row in rows:
    song=row.split(',')
    songs.append(song)
print(songs)

print ('hello2')

ports = list(serial.tools.list_ports.comports())
print (ports)
for p in ports:
    print (p[1])
    if "SERIAL" in p[1] or "Serial" in p[1]:
	    ser=serial.Serial(port=p[0])
    else :
	    print ("No Arduino Device was found connected to the computer")

#song1 = ['star','1','1','5','5','6','6','5','5','4','4','3','3','2','2','1','1']
#song2 = ['hallo','1','2','3','1','1','2','3','1','3','4','5','3','4','5']

f = open('mysongs.csv', 'r')
data = f.read()
rows = data.split('\n')
print(rows[0:5])

=======
>>>>>>> 956811d1e5789db86eb3e8297c0f0d46e2f7d2e0
#songs_dictionary={'tinklestar':1,'dadaotuhao':2,'RadetzkyMarsch':3,'xjbsong':4,'clash royale':5}

def run():

mysongs_data=[]
f=open("mysongs.csv","r")
data =  f.read()
rows = data.split('\n')
for row in rows:
    split_row = row.split(",")
    mysongs_data.append(split_row)
for row in songs_data:
    mysongs.append(row[1])
count = 0
for item in  mysongs:
    count = count + 1
new_mysongs = songs[1:6]

    action = "empty"
    while action != "q":
        print ('select 1.input song sequence, number,select 2 , input song namen , q and others for quit')
        action = input("> ")
        if action=='1' :
        print ('select in which song do you want to play:for example：1,2,3,4,5, q and others for quit')
        song_number = int(input("> "))
            print("song number is:")
            print(song_number)
            for notes in songs[song_number]:
                if notes.isdigit():
                    ser.write(notes.encode())
                    print ("send:"+notes)
                    ser.write("A".encode())
                    print ("send:A")
                    if int(notes) < 40:
                        time.sleep(0.1)
        elif action == "2":
            print ('select in which song do you want to play:tinklestar,dadaotuhao,RadetzkyMarsch,xjbsong,clash royale,q and others for quit')
            song_name = input("> ")
            import pandas as pd
            mysongs=pd.read_csv('mysongs.csv')
            import numpy as np
            print ('select in which song do you want to play:for example：1,2,3,4,5, q and others for quit')
            song_number = int(input("> "))
            songs_name_row = mysongs.loc[song_number]
            print("songs name is:")
            print(songs_name_row)
            song_number=songs_dictionary[song_name]
            print("song number is:")
            print(song_number)
            for notes in songs[song_number]:
                ser.write(notes.encode())
                print ("send:"+notes)
                time.sleep(1)
        else :
            return

run()
