#链表/

listT1 = ["a","b","c","d","e","f"]
print(listT1)
print(listT1[-1])
listT1.append("g")
print(listT1)


del listT1[0]
print(listT1)

tpl = listT1.pop()
print(tpl)
print(listT1)
tp2 = listT1.pop(0)
print(tp2)
tp3= listT1.pop(1)
print(tp3)
print(listT1)