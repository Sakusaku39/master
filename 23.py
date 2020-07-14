#記事中に含まれるセクション名とそのレベル（例えば”== セクション名 ==”なら1）を表示せよ．

import read20
import re

text = read20.file_reading()
text = text.split('\n')
"""
for line in text:
    if re.match(r'^(={2,})\s*(.+)\s*', line):
        print(line)
"""
def SectionLevel(line):
    section = re.split('(={2,})|\s+', line)
    return section

for line in text:
    if re.match(r'^(={2,})(\w+)(={2,})$', line):
        #print(line)
        section = SectionLevel(line)
        #print(section)
        level= len(section[1]) - 1
        #print(level)
        print('「{section}」のセクションレベルは{level}'.format(section=section[2], level=level))
