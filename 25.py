#記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ．

import read20
import re

text = read20.file_reading()
text = text.split('\n')
template_dictionary = {}
"""
def basic_information(line):
    data = re.split('=', line)
    return data
"""

for line in text:
    if re.match(r'^\|\w+', line):
        data = re.search('^\|(\w+)\s*\=\s*(.+)', line)  #???????????????
        print(data.groups())
        """
        key = re.sub('[\|\s]','',data[0])
        value = data[1]
        template_dictionary[key] = value

print(template_dictionary)
"""
"""
for key,value in template_dictionary.items():
"""
