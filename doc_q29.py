d={"J":1,"y":2,"o":3,"t":4,"i":5}
l=list(d.keys())
l.sort()
dic={}
for i in l:
    dic[i]=d[i]
print(dic)
