#名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．


import nlp100_30
neko_data = nlp100_30.reading_data()

for line in range(len(neko_data)):
    if neko_data[line]['pos'] == '名詞' and neko_data[line+1]['pos'] == '名詞': #2連続で名詞が出たらとりあえず出力
        print(neko_data[line]['surface']+neko_data[line+1]['surface'])
        for num in range(2, len(neko_data) - line):
            if neko_data[line+num]['pos'] == '名詞':  #3つ目以降も名刺なら続けて出力
                print(neko_data[line+num]['surface'], end='')   #改行しないように一応してみた
            else:
                break
