"""
「猫」とよく共起する（共起頻度が高い）10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．
  共起頻度とは，文章の中で「同時に使われやすい言葉」
"""
import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib    #豆腐文字っていうのになったから仕方なく
import re
from collections import defaultdict
import nlp100_30
neko_data = nlp100_30.reading_data()

sentence = []
sentences = []
for data in neko_data: #リストの中のリスト
    sentences.append(sentence)
    sentence = []
    for num in data:    #リストの中の辞書
        if re.search(r'\w+', num['surface']):    #他の記号は省く？
            sentence.append(num['surface'])
        else:
            continue
#print(sentence)
word_count = defaultdict(int)
for words in sentences:
    if "猫" in words and 2 <= len(words):
        for word in words:
            if word == "猫":
                continue
            else:
                word_count[word] += 1
    else:
        continue
left = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
label = []
height = []
for key, value in sorted(word_count.items(), key = lambda x: x[1], reverse=True):
    label.append(key)
    height.append(value)

left = np.array(left)
height = np.array(height[:10])

plt.bar(left, height, tick_label=label[:10], align="center")
#plt.show()
plt.savefig("/Users/skr/Desktop/100/result/filename37.png")
#print(label[:10], height)
