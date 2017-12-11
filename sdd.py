stop_words=[]
stop_words_list='cn_stop_words.txt'
f=open(stop_words_list,encoding='utf-8')
stop_lines=f.readlines()
for stop_line in stop_lines:
    stop_words.append(stop_line.strip('\n'))
print(stop_words)