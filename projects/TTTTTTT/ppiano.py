import serial
import serial.tools.list_ports
import time

f = open('mysongs.csv', 'r')
data = f.read()
rows = data.split('\n')
print(rows[0:5])

print("Hello")

songs=[]
for row in rows:
    song=row.split(',')
    songs.append(song)
print(songs)

lines = []

print("Hello Again")
for xxx in songs:
    lines.append(xxx[0])
print(lines[3])

def song_dictionary():
    dictionary = {}
    for n in range(len(songs)):
        song = songs[n]
        song_name = song[0]
        dictionary[song_name]= n
    return dictionary





print ('hello')
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





#songs_dictionary={'tinklestar':1,'dadaotuhao':2,'RadetzkyMarsch':3,'xjbsong':4,'clash royale':5}

#song_dic={'tinkelstar':1,'dadaotuhao':2,'RadetzkyMarsch':3,'RadetzkyMarsch2':4,'xjbsong':5,'clash royale':6}
#ser=serial.Serial(port='COM4')
#ser=serial.Serial(port]='/dev/ttymodem542')
#ifha;oifhad;oifh
def run():

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
                    if int(notes)< 40:
                        time.sleep(0.5)
                    else:
                        time.sleep(0.1)
                else:
                    time.sleep(1)


        elif action == "2":
            print ('select in which song do you want to play:tinklestar,dadaotuhao,RadetzkyMarsch,xjbsong,clash royale,q and others for quit')
            song_name = input("> ")
            print("songs name is:")
            print(song_name)
            print(song_dictionary)
            song_dic=song_dictionary()
            song_number = song_dic[song_name]
            print("song number is:")
            print(song_number)
            for notes in songs[song_number]:
                if notes.isdigit():
                    ser.write(notes.encode())
                    print ("send:"+notes)
                    ser.write("A".encode())
                    if int(notes)< 40:
                        time.sleep(0.5)
                    else:
                        time.sleep(0.1)
                else:
                    time.sleep(1)
        else :
            return
run()
