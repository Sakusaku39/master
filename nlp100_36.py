#出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．


import numpy as np
import matplotlib.pyplot as plt
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

s = sorted(word_count.items(), key = lambda x: x[1], reverse=True)
left = []
label = []
height = []
top_s = s[0:10]
#print(top_s)
for num in top_s:
    left.append(0)
    label.append(num[0])
    height.append(num[1])
left = np.array(left)
height = np.array(height)

plt.bar(left, height, tick_label=label, align="center")
plt.show()
