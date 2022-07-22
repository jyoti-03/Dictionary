dic={'Alex':['subj1','subj2','subj3'],'David':['subj1','subj2']}
c=0
for d in dic:
    for i in dic[d]:
        c+=1
print(c)
