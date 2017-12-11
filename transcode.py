import os
import codecs

filenames = os.listdir(os.getcwd())

out = file("name.txt", "w")
for filename in filenames:
    out.write(filename.decode("gb2312").encode("utf-8"))
out.close()