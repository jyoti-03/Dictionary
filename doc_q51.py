# a={'v':[1,4,6,10],'v1':[1,4,12],'v11':[1,3,8]}
a={'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}
dic={}
for i in a.keys():
    b=[]
    for j in a[i]:
        if j%2==0:
            b.append(j)
        dic[i]=b
print(dic)

# o/p= {'V': [4, 6, 10], 'VI': [4, 12], 'VII': [8]}
# o/p={'V': [], 'VI': [], 'VII': [2]}