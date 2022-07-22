dic={'c1':[1,2,3],'c2':[5,6,7],'c3':[9,10,11]}
for i in dic:
    print(i,end=" ")
print()
a=[]
for i in dic:
    b=dic[i]
    a.append(b)
    # print(b)
# print(a)
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j],end=" ")
    print()


