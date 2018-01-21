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
#songs_dictionary={'tinklestar':1,'dadaotuhao':2,'RadetzkyMarsch':3,'xjbsong':4,'clash royale':5}

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
                    print ("send:A")
                    if int(notes) < 40:
                        time.sleep(0.5)
                    elif int(notes)> 40:
                        LED={}
                        LED["start_fan"]=41
                        LED["stop_fan"]=42
                        LED["start_LED"]=43
                        LED["stop_LED"]=44
                        LED["vary_the_color_of_the_LED"]=45
                        LED["stop_45"]=46
                        start_fan=LED["start_fan"]
                        stop_fan=LED["stop_fan"]
                        start_LED=LED["start_LED"]
                        stop_LED=LED["stop_LED"]
                        vary_the_color_of_the_LED=LED["vary_the_color_of_the_LED"]
                        stop_45=LED["stop_45"]

        else :
            return

run()
