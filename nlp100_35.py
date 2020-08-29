#文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べよ．


import re
import nlp100_30

def count():
    neko_data = nlp100_30.reading_data()
    word_count = {}
    for data in neko_data:
        for line in data:
            if re.search(r'\w+', line['surface']):
                word = line['base']
                word_count[word] = word_count.get(word, 0) + 1  # 初めて辞書に登録する単語は0+1になる
            else:
                continue
    #print(word_count)
    return word_count

if __name__ == '__main__':
    word_count = count()
    for key, value in sorted(word_count.items(), key = lambda x: x[1], reverse=True):
        print(str(value) + " " + str(key))
