import json

dc1 = "../resource/test.json"

dc2 = "../resource/test2.txt"

with open(dc1) as FileTp1:
    Numbers = json.load(FileTp1)
print(Numbers)


with open(dc2) as FileTp2:
    Content = FileTp2.read()
print(Content)