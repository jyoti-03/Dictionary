# d={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
d={'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}
l=[]
for k in d:
    li=[]
    li.append(k),li.append(d[k])
    l.append(li)
print(l)

# o/p=[[1, 'red'], [2, 'green'], [3, 'black'], [4, 'white'], [5, 'black']]
# o/p=[['1', 'Austin Little'], ['2', 'Natasha Howard'], ['3', 'Alfred Mullins'], ['4', 'Jamie Rowe']]
