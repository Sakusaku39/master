#記事中でカテゴリ名を宣言している行を抽出せよ．

import gzip
import json

with gzip.open('/Users/skr/Desktop/100/jawiki-country.json.gz','r','utf-8') as f:
    for l in f:
        j = json.loads(l)


print()
