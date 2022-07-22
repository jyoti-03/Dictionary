d= {1:10,2:20,3:30,4:40,5:50,6:60}
lw=["key","value","count"]
lk=list(d.keys())
lv=list(d.values())
for w in lw:
    print(w,end=" ")
print()
c=0
for k in lk:
    print(k," ",lv[c]," ",c+1)
    c+=1
