import serial
import serial.tools.list_ports
import time

print ('hello')
ports = list(serial.tools.list_ports.comports())
print (ports)
for p in ports:
    print (p[1])
    if "Arduino" in p[1]:
	    ser=serial.Serial(port=p[0])
    else :
	    print ("No Arduino Device was found connected to the computer")

song1 = ['star','1','1','5','5','6','6','5','5','4','4','3','3','2','2','1','1']
song2 = ['hallo','1','2','3','1','1','2','3','1','3','4','5','3','4','5']


f = open("mysongs.csv")
data = f.read()
numbers = data.split('\n')
song1 = numbers[0].split(',')


f = open('mysongs.csv', 'r')
data = f.read()
rows = data.split('\n')
print(rows[0:5])
row=rows[0]
song3 = row.split(',')

songs=[]
for row in rows:
    song=row.split(',')
    songs.append(song)
print(songs)

album={}
album["tinkelstar"]=0
n=0
for song in songs:
    songname=song[0]
    print("songname is %s" %(songname))
    album[songname]=n
    n=n+1
print(album)

songid1=album["tinkelstar"]
print("songid is %d\n" %(songid1))

#ser=serial.Serial(port='COM4')
#ser=serial.Serial(port]='/dev/ttymodem542')
#ifha;oifhad;oifh
def run():
    action = "empty"
    while action != "q":
        print ('select which number of song do you want to play ? 1,2 q and others for quit')
        action = input("> ")
        if action == "1":
            song_number=input('>>')
            print("song number is:")
            print(song_number)
            song1=songs[song_number]
            for notes in song1:
                ser.write(notes.encode())
                print ("send:"+notes)
                time.sleep(1)
        elif action == "2":
            print('Please input the name')
            song_name= input('>>>')
            print('song_name is:')
            print(song_name)
            song_dic={
                'tinkelstar':1,
                'dadaotuhao':2,
                'RadetzkyMarsch':3,
                'RadetzkyMarsch2':4,
                'xjbsong':5,
                'clash':6
            }
            song_number=song_dic[song_name]
            print(song_number)
            song1=songs[song_number]
            for notes in song1:
                ser.write(notes.encode())
                print ("send:"+notes)
                time.sleep(1)

        else :
            return

run()
