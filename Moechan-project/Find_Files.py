from glob import glob

class find_files():
    def find():
        PATH = ".\\Music\\*.wav"
        result = glob(PATH)
        print('\n===[wav-list]=================' + '='*30)
        count = 0
        for music in result:
            count += 1
            print(str(count) +' : '+ music.replace('.\\Music\\', ''))
        print('='*60)
        return result

    def read_text():
        playlist = f.read().split('\n')
        print(playlist)
        return playlist