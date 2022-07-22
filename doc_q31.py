dic={'item1':45.50,'item2':35,'item3':41.30,'item4':55,'item5':24}
l=list(dic.values())
l.sort(reverse=True)
d=[]
k=[]
for j in l:
    for k in dic:
        if dic[k]==j:
            d.append(k)
list=[]
i=0
for li in d:
    list.append(li)
    print(li,l[i])
    i+=1
    if len(list)==3:
        break
# print(list)
