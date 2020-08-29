#2つの名詞が「の」で連結されている名詞句を抽出せよ．
"""
#表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）

私の楽器
私	名詞,代名詞,一般,*,*,*,私,ワタシ,ワタシ
の	助詞,連体化,*,*,*,*,の,ノ,ノ
楽器	名詞,一般,*,*,*,*,楽器,ガッキ,ガッキ
"""

import nlp100_30
neko_data = nlp100_30.reading_data()

for data in neko_data:
    for line in range(1, len(data)-1):
        if 3 > len(data):
            continue
        else:
            if data[line-1]['pos'] == '名詞' and data[line]['surface'] == 'の' and data[line]['pos1'] == '連体化' and data[line+1]['pos'] == '名詞':
                print(data[line-1]['surface'] + data[line]['surface'] + data[line+1]['surface'])
            else:
                continue
