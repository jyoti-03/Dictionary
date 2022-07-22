# dic={'key1':1,'key2':3,'key3':2}
# dic2={'key1':1,'key2':2}
# dk=list(dic.keys())
# dk2=list(dic2.keys())
# l=[]
# for dick in dk:
#     if dick in dk2:
#         l.append(dick)
# # print(l)
# for d in dic2:
#     for d2 in l:
#         if dic2[d2] == dic[d]:
#             print(d2,":",dic2[d2],"is present in both dic1 and dic2")

x={'key1':1,'key2':3,'key3':2}
y={'key1':1,'key2':2}
for i in x:
    for j in y:
        if i==j and x[i]==y[j]:
            print(i,":",x[i],'is presented in x and y both')

