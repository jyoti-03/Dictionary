# a=[{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]    
# cp={}
# val=0
# for d in a:
#     if d['item'] not in cp:
#         cp[d['item']] = d['amount']
#     else:
#         cp[d['item']] += d['amount'] 
# print(cp)

l= [{'item': 'item1', 'amount': 400},{'item': 'item2', 'amount': 300},{'item': 'item1', 'amount': 750}]
nl = []
for li in l:
    nl.append(list(li.values()))
d= {}
for t in nl:
    if t[0] in d:
        d[t[0]] += t[1]
    else:
        d[t[0]] = t[1]
print(d)
