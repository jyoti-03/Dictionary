dic={'a':5,'b':14,'c':32,'d':35,'e':24,'f':100,'g':57,'h':8,'i':100}
n=int(input("Enter how many number u want-: "))
a=list(dic.values())
a.sort(reverse=True)
# print(a)
l=[]
for v in a:
    for k in dic:
        if dic[k] == v:
            if k not in l:
                l.append(k)
                if len(l) == n:
                    break
    if len(l)==n:
        break

print(l)

# o/p = input-5 ,o/p-['f', 'i', 'g', 'd', 'c']
