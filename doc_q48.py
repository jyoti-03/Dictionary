# d={'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}
d={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
dic={}
for v in d.values():
    c=0
    for i in range(len(v)):
        c+=1
    dic[v]=c
print(dic)

# o/p={'red': 3, 'green': 5, 'black': 5, 'white': 5}
# o/p={'Austin Little': 13, 'Natasha Howard': 14, 'Alfred Mullins': 14, 'Jamie Rowe': 10}