d={'Cierra Vega':(6.2,70),'Alden Cantrell':(5.9,65),'Kierra Gentry':(6.0,68),'Pierre Cox':(5.8,66)}
dic={}
for k in d:
    for v in d.values():
        # print(v)
        if v[0]>=6 and v[1]>=70:
            if d[k] == v:
                dic[k]=v
print(dic)

