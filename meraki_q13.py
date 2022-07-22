dic={'a':50,'b':58,'c':56,'d':40,'e':100,'f':20}
l=list(dic.values())
l.sort(reverse=True)
d=[]
k=[]
for j in l:
    for k in dic:
        if dic[k]==j:
            d.append(k)
list=[]
for li in d:
    list.append(li)
    if len(list)==3:
        break
print(list)