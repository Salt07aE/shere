import subprocess
import winsound
from datetime import datetime


def jtalk(t):
    # depend on your install folder 
    OPENJTALK_BINPATH = 'c:/open_jtalk/bin'
    OPENJTALK_DICPATH = 'c:/open_jtalk/bin/dic'
    OPENJTALK_VOICEPATH = 'C:/open_jtalk/bin/mei_bashful.htsvoice'
    open_jtalk=[OPENJTALK_BINPATH + '/open_jtalk.exe']
    mech=['-x',OPENJTALK_DICPATH]
    htsvoice=['-m',OPENJTALK_VOICEPATH]
    speed=['-r','1.2']
    pech=['-fm','1.7']
    F0=['-jf','0.5']
    outwav=['-ow','open_jtalk.wav']
    cmd=open_jtalk+mech+htsvoice+speed+pech+F0+outwav
    c = subprocess.Popen(cmd,stdin=subprocess.PIPE)

    # convert text encoding from utf-8 to shitf-jis
    c.stdin.write(t.encode('shift-jis'))
    c.stdin.close()
    c.wait()

    # play wav audio file with winsound module
    winsound.PlaySound('open_jtalk.wav', winsound.SND_FILENAME)


def say_datetime():
    d = datetime.now()
    text = '%s月%s日、%s時%s分%s秒' % (d.month, d.day, d.hour, d.minute, d.second)
    print(text)
    jtalk(text)

if __name__ == '__main__':
    say_datetime()