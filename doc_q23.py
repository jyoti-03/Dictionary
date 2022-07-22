dic={'a':50,'b':580,'c':560,'d':400,'e':100,'f':200}
l=list(dic.values())
l.sort(reverse=True)
d=[]
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

