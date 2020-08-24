#文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べよ．


import re
import nlp100_30
neko_data = nlp100_30.reading_data()

word_count = {}
for line in neko_data:
    if re.search(r'\w+', line['surface']):
        word = line['surface']
        word_count[word] = word_count.get(word, 0) + 1  # 初めて辞書に登録する単語は0+1になる
    else:
        continue
    #print(word_count)
for key, value in sorted(word_count.items(), key = lambda x: x[1], reverse=True):
    print(str(value) + " " + str(key))
