import pandas as pd
import csv

class char_csv:
    def log():
        print("キャラクター情報を参照します。\n参照したいキャラクター名を入力してください。")
        char_name = input("キャラクター名：")
        print("")
        with open('character-sheet.csv') as char_sheet_csv_r:
            df = pd.read_csv('character-sheet.csv', index_col=0)
            exist = df[df.name == char_name]
            if len(exist) == 0:
                logNone = "キャラクター["+ char_name +"]は存在しません。"
                return logNone
            return exist
