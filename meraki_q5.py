l1=["one","two","three","four","five"]
l2=[1,2,3,4,5,]
l={}
for i in l1:
    for j in l2:
        l[i]=j
        l2.remove(j)
        break
print(l)
