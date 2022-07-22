d={"c1":[1,2,3],"c2":[4,5,6],"c3":[7,8,9]}
for k in d:
   for  v in d[k]:
       d[k].clear()
print(d)

# o/p={"c1":[],"c2":[],