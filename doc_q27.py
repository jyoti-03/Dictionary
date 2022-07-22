l=[{'id': 1, 'success': True, 'name': 'Lary'},{'id': 2, 'success': False, 'name': 'Rabi'},{'id': 3, 'success': True, 'name': 'Alex'}]
c = 0
n=input("enter-: ")
for d in l:
    if n in d:
        if type(d[n]) == int:
            c+=d[n]
        if type(d[n])== str:
            print(d[n],end=" ")
        if type(d[n])==bool:
            c+=d[n]
if type(d[n])==str:
    pass
else:
    print(c)
    