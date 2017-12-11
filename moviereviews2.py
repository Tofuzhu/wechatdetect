from urllib import request
from bs4 import BeautifulSoup as bs
import jieba
import os
from collections import Counter
import time
import re
stop_words=[]
stop_words_list='cn_stop_words.txt'
f=open(stop_words_list,encoding='utf-8')
stop_lines=f.readlines()
for stop_line in stop_lines:
    stop_words.append(stop_line.strip('\n'))
print(stop_words)


pageNum=1
eachCommentList=[]
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'}
while pageNum<=10:
    start=(pageNum-1)*20
    requrl= 'https://movie.douban.com/subject/' + '25858758' + '/comments' + '?' + 'start='+str(start) + '&limit=20'
    print(requrl)
    respp = request.Request(url=requrl,headers=headers)
    resp=request.urlopen(respp)
    html_data = resp.read().decode('utf-8')
    soup = bs(html_data, 'html.parser')
    comment_div_lits = soup.find_all('div', class_='comment')
    for item in comment_div_lits:
        if item.find_all('p')[0].string is not None:
            eachCommentList.append(item.find_all('p')[0].string)
    pageNum=pageNum+1
    print(eachCommentList)
    #time.sleep(2)


tokens=[]
for line in eachCommentList:
    clean_line = str(line).strip()
    pattern = re.compile(r'[\u4e00-\u9fa5]+')
    filterdata = re.findall(pattern, clean_line)
    clean_line = ''.join(filterdata)
    if len(clean_line) > 0:
        seg_list = jieba.cut(clean_line)
        for seg in seg_list:
            if seg not in stop_words:
                tokens.append(seg)



print(tokens)

counter = Counter(tokens)
for a in counter.most_common(20):
    print(a[0] + '\t' + str(a[1]))
