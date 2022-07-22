l=['S001', 'S002', 'S003', 'S004']
li=['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
lis=[85, 98, 89, 92]
dic=[]
for d in li:
    di={}
    for dl in lis:
        di[d]=dl
    dic.append(di)
# print(dic)
d=dict(zip(l,dic))
print(d)

