import trpg_dice
import trpg_charlog
import numpy as np
import pandas as pd
import csv

class TRPG():
    def crt_char():
        STR = trpg_dice.diceroll(3,6).roll()[1]
        print("STR (筋力) 3D6：{}".format(STR))
        CON = trpg_dice.diceroll(3,6).roll()[1]
        print("CON (体力) 3D6：{}".format(CON))
        POW = trpg_dice.diceroll(3,6).roll()[1]
        print("POW (精神力) 3D6：{}".format(POW))
        DEX = trpg_dice.diceroll(3,6).roll()[1]
        print("DEX (俊敏性) 3D6：{}".format(DEX))
        APP = trpg_dice.diceroll(3,6).roll()[1]
        print("APP (外見) 3D6：{}".format(APP))
        SIZ = trpg_dice.diceroll(2,6).roll()[1] + 6
        print("SIZ (体格) 2D6+6：{}".format(SIZ))
        INT = trpg_dice.diceroll(2,6).roll()[1] + 6
        print("INT (知性) 2D6+6：{}".format(INT))
        EDU = trpg_dice.diceroll(3,6).roll()[1] + 3
        print("EDU (教育) 3D6+3：{}".format(EDU))
        money = trpg_dice.diceroll(3,6).roll()[1]
        print("年収・財産 3D6：{}".format(INT))
        san = POW * 5
        print("san値 POW x 5 : {}".format(san))
        luck = POW * 5
        print("幸運 POW x 5 : {}".format(luck))
        idea = INT * 5
        print("アイデア INT x 5 : {}".format(idea))
        know = EDU * 5
        print("知識 EDU x 5 : {}".format(know))
        edr = (CON + SIZ) / 2
        print("耐久値 CON + SIZ ÷ 2 : {}".format(edr))
        mp = POW
        print("マジックポイント (POW) : {}".format(mp))
        ptp = EDU * 20
        print("職業技能ポイント (EDU x 20) : {}".format(ptp))
        htp = INT * 10
        print("趣味技能ポイント (INT x 10) : {}".format(htp))
        db = STR + SIZ
        dpb = []
        if db < 13:
            dpb = [-1, 4]
        elif db < 17:
            dpb = [-1, 6]
        elif db < 25:
            dpb = [0,0]
        elif db < 33:
            dpb = [1, 4]
        elif db < 41:
            dpb = [1, 6]
        elif db < 57:
            dpb = [2, 6]
        else:
            dpb = [3, 6]
        print("ダメージポイントボーナス : {}D{}".format(dpb[0], dpb[1]))


        while True:
            print("\nファイルに出力しますか？")
            x = input("1. yes  2. no :")
            if x == "1":
                flag2 = 0
                with open('character-sheet.csv') as char_sheet_csv_r:
                    df = pd.read_csv('character-sheet.csv', index_col=0)
                    id_csc = len(df)

                with open('character-sheet.csv') as char_sheet_csv_r:
                    while True:
                        print("\nキャラクター名を入力してください。\n(!cancelと入力で登録を取りやめます)　")
                        char_name = input("キャラクター名：")
                        df = pd.read_csv('character-sheet.csv', index_col=0)
                        exist = df[df.name == char_name]
                        flag = len(exist)

                        if char_name == '!cancel':
                            flag2 = 1
                            print("登録をやめました。")
                            break

                        if flag == 0:
                            break

                        print("\nその名前のキャラクター名は既に存在しています。")

#                char_list = ['キャラクター名 : ', char_name,'\n', 'STR : ', str(STR), '\n', 'CON : ', str(CON), '\n', 'POW : ', str(POW), '\n', 'DEX : ', str(DEX), '\n', 'APP : ', str(APP), '\n', 'SIZ : ', str(SIZ), '\n', 'INT', str(INT), '\n', 'EDU : ', str(EDU), '\n', '年収・財産 : ', str(money), '\n', 'san値：', str(san), '\n', '幸運：', str(luck), '\n', 'アイデア：', str(idea), '\n', '知識：', str(know), '\n', '耐久値:', str(edr), '\n', 'マジックポイント：', str(mp), '\n', '職業技能ポイント：', str(ptp), '\n', '趣味技能ポイント：', str(htp), 'ダメージポイントボーナス：', str(dpb)'\n\n']
                char_csv = {'num':id_csc, 'name':char_name, 'id':id_csc, 'STR':STR, 'CON':CON, 'POW':POW, 'DEX':DEX, 'APP':APP, 'SIZ':SIZ, 'INT':INT, 'EDU':EDU, 'money':money, 'san':san, 'luck':luck, 'idea':idea, 'know':know, 'edr':edr, 'mp':mp, 'ptp':ptp, 'htp':htp, 'dpb':dpb}
                flag2 = TRPG.file_w_r(char_csv, flag2)
                if flag2 == 1:
                    break

            elif x == "2":
                break

            
            print("\n間違った値が入力されています。")

                

    def file_w_r(char_csv, flag2):
        if flag2 == 0:
#            with open('character-sheet.txt', 'a') as char_sheet_text:
#                char_sheet_text.writelines(char_list)

            with open('character-sheet.csv', 'a', newline = "") as char_sheet_csv:
                writer = csv.DictWriter(char_sheet_csv, ['num', 'name', 'id', 'STR', 'CON', 'POW', 'DEX', 'APP', 'SIZ', 'INT', 'EDU', 'money', 'san', 'luck', 'idea', 'know', 'edr', 'mp', 'ptp', 'htp', 'dpb'])
                writer.writerow(char_csv)

            print("登録が完了しました！")
            flag2 = 1
            return flag2

        elif flag2 == 1:
            flag2 = 1
            return flag2



    def main():
        while True:
            print("何をしますか？数字を入力してください。")
            sentaku1 = input("1.ダイス 2.キャラ作成 3.キャラ参照 4.プログラム終了：")
            print("")
            if sentaku1 == "1":
                count_char = input("ダイスを振る回数を入力してください。　：")
                count = int(count_char)
                men_char = input("ダイスの目の数を入力してください。　：")
                men = int(men_char)

                print("\n{}D{}".format(count,men))

                result = trpg_dice.diceroll(count,men).roll()
                result_dice = result[0]
                result_all = result[1]

                print("ログ：{}".format(result_dice))
                print("結果：{}".format(result_all))

            elif sentaku1 == "2":
                TRPG.crt_char()

            elif sentaku1 == "3":
                log = trpg_charlog.char_csv.log()
                print(log)

            elif sentaku1 == "4":
                print("プログラムを終了します。")
                break

            print("")
