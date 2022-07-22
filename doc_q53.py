l=[[1,'Jean Castro','V'],[2,'Lula Powell','V'],[3,'Brian Howell','VI'],[4,'Lynne Foster','VI'],[5,'Zachary Simon','VII']]
d={}
for k in l:
    c=k[0]
    k.remove(k[0])
    d[c]=k
print(d)

# o/p = {1: ['Jean Castro', 'V'], 2: ['Lula Powell', 'V'], 3: ['Brian Howell', 'VI'], 4: ['Lynne Foster', 'VI'], 5: ['Zachary Simon', 'VII']}