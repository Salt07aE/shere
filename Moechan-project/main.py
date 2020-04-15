import recognizer as re
import Moe_df as Md
import Moe_module as Mm
import Moe_jtalk as Mj
import Text_Input as debug

class Moechan_project():
    def main():
        while True:
            text = debug.Text_Input.input()
            #text = re.Recognizer.main()
            print("You said : " + text)
            if text == 'Error':
                continue
            response = Md.Dialogflow(text).main()
            res_text = response[0]
            flag = response[1]
            print('モエちゃん：' + res_text)
            print('=' * 20)
            if res_text == 'time-now':
                Mm.Module.time_now()

            if res_text == 'あいさつ':
                Mm.Module.greeting()
            
            if res_text == 'TRPG':
                Mm.Module.trpg()
                
            else:
                if len(res_text) == 0: 
                    continue
                Mj.jtalk(res_text)

            if flag  == 1:
                break


Moechan_project.main()