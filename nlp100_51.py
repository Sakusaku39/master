"""
学習データ，検証データ，評価データから特徴量を抽出し，それぞれtrain.feature.txt，valid.feature.txt，test.feature.txtというファイル名で保存せよ．
なお，カテゴリ分類に有用そうな特徴量は各自で自由に設計せよ．
記事の見出しを単語列に変換したものが最低限のベースラインとなるであろう．
"""
import nltk
import re
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')

#NLP = "Natural language processing (NLP) is a subfield of linguistics, computer science, information engineering, and artificial intelligence concerned with the interactions between computers and human (natural) languages, in particular how to program computers to process and analyze large amounts of natural language data."

def clearn(text):
    text = re.sub(r'\W', ' ', text)
    return text

infile = ['test.txt','train.txt','valid.txt']
#outfile = ['test.feature.txt','train.feature.txt','valid.feature.txt']
#for input, output in zip(infile, outfile):
for input in infile:
    with open(input, 'r') as inf:
        datas = []
        category = {}
        for line in inf:
            data = line.split('\t')
            #print(data)
            datas.append(data)
            #category.update(data[0])
        #category = ['b','t','e','m']
        #for ctg in category:
            #ctg = []    #これでいいのか
            b = []
        for data in datas[:10]:
            datafirst = clearn(data[1])
            datafirst = word_tokenize(datafirst)    #トークン化
            stop_words = stopwords.words('english') #ストップワード
            datafirst = [word for word in datafirst if word not in stop_words]  #ここ多分英語での終わりの記号っていうか目印があったらそこで終了みたいになってんのかなあとで見よ？
            porter = PorterStemmer()    #語幹抽出
            answer1 = [porter.stem(word) for word in datafirst]
            answer2 = nltk.pos_tag(datafirst) #品詞を見てる
            onlypos = [pos for part, pos in answer2]
            for genkei, pos in zip(answer1, onlypos):
                b.append([genkei, pos])
            print(b)

"""
NLP = clearn(NLP)
NLP = word_tokenize(NLP)    #トークン化
stop_words = stopwords.words('english') #ストップワード
NLP = [word for word in NLP if word not in stop_words]
#print(NLP)
porter = PorterStemmer()    #語幹抽出
answer1 = [porter.stem(word) for word in NLP]
#print(answer1)
answer2 = nltk.pos_tag(NLP) #品詞を見てる
#print(answer2)
onlypos = [pos for part, pos in answer2]
genkei_pos = []
for genkei, pos in zip(answer1, onlypos):
    genkei_pos.append([genkei, pos])
    print(genkei, pos)
"""
"""
adjective = []
noun = []
adverb = []
verb = []
for part, pos in answer2:
    if pos == 'JJ' or pos == 'JJR' or pos == 'JJS': #形容詞
        adjective.append(part)
    elif pos == 'NN' or pos == 'NNS' or pos == 'NNP' or pos == 'NNPS': #名詞
        noun.append(part)
    elif pos == 'RB' or pos == 'RBR' or pos == 'RBS': #副詞
        adverb.append(part)
    elif pos == 'VB' or pos == 'VBD' or pos == 'VBG' or pos == 'VBN' or pos == 'VBP' or pos == 'VBZ': #動詞
        verb.append(part)
print('形容詞:{}'.format(adjective))
print('名詞:{}'.format(noun))
print('副詞:{}'.format(adverb))
print('動詞:{}'.format(verb))
"""


"""
JJ	Adjective
JJR	Adjective, comparative
JJS	Adjective, superlative

NN Noun, singular or mass
NNS Noun, plural
NNP Proper noun, singular
NNPS Proper noun, plural

RB	Adverb
RBR	Adverb, comparative
RBS	Adverb, superlative

VB	Verb, base form
VBD	Verb, past tense
VBG	Verb, gerund or present participle
VBN	Verb, past participle
VBP	Verb, non-3rd person singular present
VBZ	Verb, 3rd person singular present
"""
