d= {1:'NAVGURUKUL',2:'IN',3:{'A':'WELCOME','B':'To','C':'DHARAMSALA'}}
# del d[3]["A"]
for i,j in d.items():
    if type(j)==dict:
        d.pop(j[0])
print(d)
