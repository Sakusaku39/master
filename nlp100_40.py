'''
形態素を表すクラスMorphを実装せよ．
このクラスは表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）
をメンバ変数に持つこととする．
さらに，係り受け解析の結果（ai.ja.txt.parsed）を読み込み，
各文をMorphオブジェクトのリストとして表現し，冒頭の説明文の形態素列を表示せよ．
'''


class Morph:
    #表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）
    def __init__(self, data):
        self.surface = data['surface']
        self.base = data['base']
        self.pos = data['pos']
        self.pos1 = data['pos1']

sentences = []
morphs = []
filename = '/Users/skr/Desktop/100/ai.ja.txt.parsed'
with open(filename, 'r') as f:
    for line in f:
        if line[0] == '*':
            continue
        elif line != 'EOS\n':
            surface = line.split('\t')
            ot = surface[1].strip().split(',')  #baseに「\n*」って確か出てきてしまったから消すためにストリップ使用
            d = {'surface':surface[0], 'base':ot[6], 'pos':ot[0], 'pos1':ot[1]}
            morphs.append(Morph(d))
        else:
            sentences.append(morphs)
            morphs = []
"""全部
for i in range(0, len(sentences)):
    for num in sentences[i]:
        print(vars(num))
    #print(num.__dict__)
"""
#冒頭の説明文はリストsentenceの３個目の要素（2番目は空）
for num in sentences[2]:
    print(vars(num))
