d={'Alex':['sub1','sub2','sub3'],'David':['sub1','sub2']}
c=0
for i in d:
    for j in d[i]:
        c+=1
print(c)
