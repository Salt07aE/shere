import datetime
import trpg as t
import Moe_jtalk as Mj

class Module():
    def time_now():
        d = datetime.datetime.now()
        text = '現在、%s年%s月%s日、%s時%s分%s秒、です。' % (d.year, d.month, d.day, d.hour, d.minute, d.second)
        Mj.jtalk(text)
        return

    def greeting():
        d = datetime.datetime.now()
        if d.hour > 5 and d.hour < 10:
            text = 'おはようございますマスター。'
        elif d.hour > 5 and d.hour < 16:
            text = 'こんにちはマスター。'
        else:
            text = 'こんばんはマスター。'
        Mj.jtalk(text)
        return

    def trpg():
        text = 'TRPGプログラムを起動します。'
        Mj.jtalk(text)
        t.TRPG.main()
        text = 'TRPGプログラムを終了しました。'
        Mj.jtalk(text)
        return