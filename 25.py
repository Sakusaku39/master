#記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ．

import read20
import re
import pprint

text = read20.file_reading()
template_dictionary = {}

#def basic_information(line):

basic_information = re.search(r'^\{\{基礎情報\s国\n(.*)\n\}\}$', text, re.MULTILINE + re.DOTALL)
#print(basic_information.group(1))
basic_data = basic_information.group(1)
basic_data = basic_data.split("\n")
#print(basic_data)

for line in basic_data:
    data = re.match(r'^\|(.+?)\s*\=\s*(.*)', line, re.DOTALL)  #???????????????
    if data == None:
        continue
    else:
        key = re.sub('\|','',data.group(1))
        key = re.sub('\s$','',key)
        value = data.group(2)
        #print(value)
        template_dictionary[key] = value
#print(template_dictionary)
pprint.pprint(template_dictionary, width=400)
#pprint.pformat(template_dictionary, sort_dicts = False)