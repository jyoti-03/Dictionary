dic={'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}
lv=list(dic.values())
l=len(lv)
c=0
e=lv[c]
for v in range(len(lv)):
    if lv[v]==e:
        c+=1
if l==c:
    print(True)
else:
    print(False)

