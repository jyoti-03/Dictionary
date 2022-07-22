num_list = [1, 2, 3, 4]
c={}
dic=c
for i in num_list:
    c[i]={}
    c=c[i]
print(dic)
# o/p={1: {2: {3: {4: {}}}}}