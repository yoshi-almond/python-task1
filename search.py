# -*- coding:utf-8 -*-
import csv

def search_word(src,path):
    word = input("鬼滅の登場人物の名前を入力してください >>> ")
    if word in src:
        print(word+'が見つかりました')
    else:
        print(word+'は見つかりませんでした')
        while True:
            add_ans = input(word+'を追加しますか？(y/n) >>')
            if add_ans == 'y':
                src.append(word)
                with open(path, 'w') as f:
                    w = csv.writer(f)
                    w.writerow(src)
                print(word+'を新しく追加しました')
                break
            elif add_ans == 'n':
                print(word+'を追加しませんでした')
                break
            else:
                print('もう一度入力をお願いします')
                continue
