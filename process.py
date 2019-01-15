import os
import jieba
import re
import json
import pandas as pd


roots = ['一带一路', '互联网金融', '西部大开发']

for root in roots:

    # load file title
    titles = [re.sub('[0-9 \u2044]', '', f.replace('.pdf', '')) for f in os.listdir(os.path.join(root, 'pdf'))]

    # load stopwords
    stopwords = [line.strip() for line in open('stopwords.txt', 'r', encoding='utf-8').readlines()]

    word2num = {}

    # tokenize
    for title in titles:
        words = jieba.cut(title)
        words = [w for w in words if w not in stopwords]

        for word in words:
            num = word2num.setdefault(word, 0) + 1
            word2num[word] = num

    word2num = {d[0]:d[1] for d in sorted(word2num.items(), key=lambda d: d[1], reverse=True)}

    data = pd.DataFrame({'word': pd.Series(list(word2num.keys())), 'num': pd.Series(list(word2num.values()))})
    filename = root + '.csv'
    data.to_csv(filename, encoding='gbk')
    print("完成: " + filename)
