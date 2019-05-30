import json
dc1 = "../resource/test.json"

dc2 = "../resource/test2.txt"

with open(dc1,'w') as FileTp1:
    json.dump(['a','b','c'],FileTp1)


with open(dc2,'w') as FileTp2:
    FileTp2.write("hello")


with open(dc2,'a') as FileTp2:
    FileTp2.write("liuxiaoyun")