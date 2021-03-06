import serial
import serial.tools.list_ports
import time



def get_song_dictionary(input_lst):
    dictionary={}
    for i in range(len(songs)):
        song=songs[i]
        dictionary[song[0]]=i
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

song1 = ['star','1','1','5','5','6','6','5','5','4','4','3','3','2','2','1','1']
song2 = ['hallo','1','2','3','1','1','2','3','1','3','4','5','3','4','5']

f = open('mysongs.csv', 'r')
data = f.read()
rows = data.split('\n')
print(rows[0:5])

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

dic={"start_r_LED":'43',"stop_LED":'44',"start_fan":"41","stop_fan":'42',"start_g_LED":'45'}

#songs_dictionary={'tinklestar':1,'dadaotuhao':2,'RadetzkyMarsch':3,'xjbsong':4,'clash royale':5}
songs_dictionary=get_song_dictionary(songs)

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
                note=['0','0']
                if '|' in notes:
                    note=notes.split('|')
                elif '-' in notes:
                    note=notes.split('-')
                else:
                    note[0]=notes
                if note[0].isdigit():
                    ser.write(note[0].encode())
                    ser.write("A".encode())
                    print ("send:"+note[0])
                    pai=int(note[1])
                    if pai==2:
                        sl=1/2
                    elif pai==4:
                        sl=2
                    else:
                        sl=1
                    time.sleep(sl)
                else:
                    if notes in dic:
                        s_notes=dic[notes]
                        print(s_notes)
                        ser.write(s_notes.encode())
                        print ("send:"+s_notes)
                        ser.write("A".encode())
            ser.write("50".encode())
        elif action == "2":
            print ('select in which song do you want to play:tinklestar,dadaotuhao,RadetzkyMarsch,xjbsong,clash royale,q and others for quit')
            song_name = input("> ")
            print("songs name is:")
            print(song_name)
            song_number=songs_dictionary[song_name]
            print("song number is:")
            print(song_number)
            for notes in songs[song_number-1]:
                ser.write(notes.encode())
                print ("send:"+notes)
                time.sleep(1)
        else :
            return

run()
