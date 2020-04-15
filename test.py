#!python3
#coding: utf-8

#Testクラスの定義
class Test():

    #mainメソッドの定義
    def main():
        customer_list = {}#顧客リスト
        while True:
            select = input('何をしますか？\n1. 顧客データの追加\n2. 顧客データの参照\n3. プログラム終了\n\n番号を入力:')

            #顧客の氏名を入力
            if select == '1':

                #顧客データ追加システム
                name = input('\n氏名：')#顧客の名前を入力
                vertical_width = input('縦:')#土地の縦幅の入力
                horizon_width = input('横:')#土地の横幅の入力
                price = Test.calculate(vertical_width, horizon_width)

                print("{}様がご検討中の土地の値段は{}万円です。\n".format(name,price))#計算結果の表示
                customer_list[name] = price#顧客リストに追加

            elif select == '2':  print('\n' + str(customer_list) + '\n')#顧客リストの参照

            elif select == '3':  break#whileから抜けてプログラムを終了にする

            else:   print('\n【error:入力された値に間違いがあります。】\n')#1, 2, 3以外が入力されたときの対処

    #calculateメソッドの定義

    def calculate(a, b):
        #土地価格＝面積(m²)×5万円
        c = int(a) * int(b) * 5

        return c

if __name__=="__main__":

    Test.main()