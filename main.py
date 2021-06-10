# -*- coding:utf-8 -*-
import pandas as pd 
import search

#source=["ねずこ","たんじろう","きょうじゅろう","ぎゆう","げんや","かなお","ぜんいつ"]

def search():
    path = './name_list.csv'
    df = pd.read_csv(path, dtype=object)
    src = list(df['name'])
    print(src)
    word = input("鬼滅の登場人物の名前を入力してください >>> ")
    if word in src:
        print(word+'が見つかりました')
    else:
        print(word+'は見つかりませんでした')
        while True:
            add_ans = input(word+'を追加しますか？(y/n) >>')
            if add_ans == 'y':
                src.append(word)
                src = pd.DataFrame(src,columns=["name"])
                src.to_csv(path,index=False)
                print(word+'を新しく追加しました')
                break
            elif add_ans == 'n':
                print(word+'を追加しませんでした')
                break
            else:
                print('もう一度入力をお願いします')
                continue

if __name__ == "__main__":
    search()
