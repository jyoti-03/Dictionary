n=int(input("Enter number-: "))
d={}
for i in range(1,n+1):
    l=[]
    for j in range(1,11):
        l.append(i*j)
    d[i]=l
print(d)
