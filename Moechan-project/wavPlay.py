import pygame.mixer as pymix
import sys
import recognizer as re
from time import sleep
import Find_Files as ff
import msvcrt

# メイン
def main():
    pymix.init()
    sound_files = ff.find_files.find()
    select = input('please input music number : ')
    #select = re.Recognizer.main()
    if select == 'all':
        for music in sound_files:
            player(music, 0)
            flag = operate()
            if flag == 1:
                break
        return
    elif select == 'playlist1':
        playlist = ff.find_files.read_text()
        for music in playlist:
            player(music, 0)
            operate()
        return
    sound_file = sound_files[int(select) -1]
    playtype = -1
    player(sound_file, playtype)
    operate()

def player(sound_file, playtype):
    pymix.init(frequency = 44100, size = -16, channels = 2, buffer = 4096)
    print('\n【 ' + sound_file.replace('.\\Music\\', '') + ' 】\n')
    global sounds
    sounds = pymix.Sound(sound_file)
    sound_time = sounds.get_length()
    global playType
    playType = sounds.play(loops = playtype)
    print('sound time : ' + str(int(sound_time/60))+'分'+str(int(sound_time%60))+'秒')
    global svolume
    svolume = 21
    playType.set_volume(svolume/100)
    volume = playType.get_volume()
    print('volume : ' + str(int(volume*100)))

def sound_volume():
    global svolume
    svolume = input('volume : ')
    playType.set_volume(int(svolume)/100)

def operate():
    while True:
        if msvcrt.kbhit():
            command = input('\n[command] : ')
            if command == 'pause':
                pymix.pause()
            elif command == 'play':
                pymix.unpause()
            elif command == 'chack':
                w_busy =  pymix.Channel(0).get_busy()
                print(w_busy)
            elif command == 'v':
                sound_volume()
            elif command == 'l':
                playtype = input('loop : ')
                sounds.play(loops = int(playtype))
            elif command == 'stop':
                flag = 1
                pymix.stop()
                break
        if pymix.Channel(0).get_busy() == 0:
            break
    print('end')
    return flag

if __name__ == '__main__':
    main()
    pymix.stop()
    sys.exit()

#曲が終わったときにプログラムが終わらないのを直す