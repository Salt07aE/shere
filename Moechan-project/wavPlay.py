import pygame.mixer as pymix
import sys
import recognizer as re
from threading import (Event, Thread)
from time import sleep
import Find_Files as ff

# メイン
def main():
    pymix.init()
    sound_files = ff.find_files.find()
    select = input('please input music number : ')
    #select = re.Recognizer.main()
    if select == 'all':
        for music in sound_files:
            player(music, 1)
        return
    elif select == 'playlist1':
        playlist = ff.find_files.read_text()
        for music in playlist:
            player(music, 1)
        return
    player(sound_files[int(select) -1], 0)

def player(sound_file, playtype):
    pymix.init(frequency = 44100, size = -16, channels = 2, buffer = 4096)
    print('\n【 ' + sound_file.replace('.\\Music\\', '') + ' 】\n')
    sounds = pymix.Sound(sound_file)
    sound_time = sounds.get_length()
    playType = sounds.play(loops = playtype)
    print('sound time : ' + str(sound_time))
    playType.set_volume(0.1)
    volume = playType.get_volume()
    print('volume : ' + str(volume))
    thread2 = Thread(target=stop)
    thread2.start()
    operate()


def operate():
    while True:
        command = input('\n[command] : ')
        if command == 'pause':
            pymix.pause()
        elif command == 'play':
            pymix.unpause()
        elif command == 'chack':
            w_busy =  pymix.Channel(0).get_busy()
            print(w_busy)
        elif command == 'stop':
            event.set()
            break
    print('end')
    event.set()

def stop():
    while True:
        if pymix.Channel(0).get_busy() == 0:
            event.set()
            break

if __name__ == '__main__':
    event = Event()
    thread1 = Thread(target=main)
    thread1.start()
    event.wait()
    pymix.stop()

#曲が終わったときにプログラムが終わらないのを直す