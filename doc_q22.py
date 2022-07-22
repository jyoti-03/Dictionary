a={'1':['a','b'],'2':['c','d']}
b=list(a.keys())
for i in a[b[0]]:
    for j in a[b[1]]:
        print(i+j)

