"""
単語の出現頻度のヒストグラムを描け．
ただし，横軸は出現頻度を表し，1から単語の出現頻度の最大値までの線形目盛とする．
縦軸はx軸で示される出現頻度となった単語の異なり数（種類数）である．
"""

import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib
import nlp100_35
word_count = nlp100_35.count()

x = []
for key, value in word_count.items():
    x.append(value)

x = np.array(x)

print(max(x))
print(len(x))

plt.hist(x, bins = max(x), range = (1, len(x)))
#plt.xlim(xmin=1, xmax=len(x))
plt.savefig("/Users/skr/Desktop/100/result/filename38.png")
