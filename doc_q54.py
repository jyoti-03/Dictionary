dict={1:['Jean Castro'],2:['Lula Powell'],3:['Brian Howell'],4:['Lyne Foster'],5:['Zachary Simon']}
b={}
l=[]
for i in dict:
    for j in dict[i]:
        b.update({i:j})
l.append(b)
print(l)

# o/p = [{1: 'Jean Castro', 2: 'Lula Powell', 3: 'Brian Howell', 4: 'Lynne Foster', 5: 'Zachary Simon'}]