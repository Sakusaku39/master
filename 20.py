"""
Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．
問題21-29では，ここで抽出した記事本文に対して実行せよ．
"""

import json
#from collections import OrderedDict
#import pprint
import gzip

#gzip.open(filename, [mode], [compresslevel], [encoding], [errors], [newline])
with gzip.open('/Users/skr/Desktop/100/jawiki-country.json.gz','r','utf-8') as f:
    for l in f:
        j = json.loads(l)
        if j["title"] == "イギリス":
            print(j["text"])




        """
        for ["title"], ["text"] in j.items():
            if ["title"] == "イギリス":
                print(["text"])
"""
