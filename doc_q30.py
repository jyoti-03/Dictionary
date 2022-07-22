dic={'S  001':['Math','Science'],'S    002':['Math','English']}
k=list(dic.keys())
s=[]
for l in k:
    st=""
    for i in range(len(l)):
        if l[i]==" ":
            pass
        else:
            st+=l[i]
    s.append(st)
# print(s)
v=list(dic.values())
d=dict(zip(s,v))
print(d)

