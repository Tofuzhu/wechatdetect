# -*- coding: utf-8 -*-

import jieba

STOPWORDS = ['的', '地', '得', '而', '了', '在', '是', '我', '有', '和', '就', '不', '人', '都', '一', '一个', '上',
             '也', '很', '到', '说', '要', '去', '你', '会', '着', '没有', '看', '好', '自己', '这']
PUNCTUATIONS = ['。', '，', '“', '”', '…', '？', '！', '、', '；', '（', '）']

f_in = open('mao_in.txt')
f_out = open('mao_out.txt', 'w')
try:
    for l in f_in:
        seg_list = jieba.cut(l)
        # print "/".join(seg_list)

        for seg in seg_list:
            if seg not in STOPWORDS and seg not in PUNCTUATIONS:
                f_out.write(seg+"\n")

                # python seg.py && cat mao_out.txt | sort | uniq -c | sort -rg | head -5
                # 405 我们
                # 220 人民
                # 145 革命
                # 145 他们
                # 136 工作

finally:
    f_in.close()