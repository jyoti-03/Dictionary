dic={"one":1,"two":2,"three":3}
l=[]
for k in dic:
    t2=k
    t=str(dic[k])
    t3=t2,t
    l.append(tuple(t3))
print(l)