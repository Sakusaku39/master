'''
係り元の文節と係り先の文節のテキストをタブ区切り形式ですべて抽出せよ．
ただし，句読点などの記号は出力しないようにせよ．
'''

#係り受け関係：dependency relations
#係り元と係り先：a modified source and a modifying destination
import nlp100_41
data = nlp100_41.C_contact();
'''
for i in range(3):
    for chunk in data[i]:
        if int(chunk.dst) != -1:
            source = ''.join([morph.surface for morph in chunk.morphs])
            destination = ''.join([morph.surface for morph in data[i][int(chunk.dst)].morphs])
            print('{}->{}'.format(source, destination))
'''

for i in range(3):
    for chunk in data[i]:
      if int(chunk.dst) != -1:
        source = ''.join([morph.surface if morph.pos != '記号' else '' for morph in chunk.morphs])
        destination = ''.join([morph.surface if morph.pos != '記号' else '' for morph in data[i][int(chunk.dst)].morphs])
        #print('{}->{}'.format(source, destination))
        print(source, destination, sep='\t')
