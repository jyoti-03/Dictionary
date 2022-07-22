# q1
# n=int(input("Enter number-: "))
# d={}
# for x in range(1,n+1):
#     d[x]=x**2
# print(d)

# q2
# s="w3school"#input("enter any word-: ")
# d={}
# for x in s:
#     if x in d:
#         d[x]+=1
#     else:
#         d[x]=1
# print(d)

# q3
# d={'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
# vl=list(d.values())
# vl.sort(reverse=True)
# l=[]
# for v in vl:
#     for k in d:
#         if v == d[k]:
#             l.append(k)
#             print(k,v)
#             if len(l)==3:
#                 break
#     if len(l)==3:
#         break

# q4
# d={'Math':81, 'Physics':83, 'Chemistry':87}
# lv=list(d.values())
# lv.sort(reverse=True)
# l=[]
# for v in lv:
#     t=[]
#     for k in d:
#         if d[k]==v:
#             t.append(k),t.append(v)
#     l.append(tuple(t))
# print(l)

# q5
# d={"a":123,"b":456,"c":23,"d":4}
# dic={}
# for v in d:
#     vs=str(d[v])
#     s2=""
#     for s in vs:
#         # print(s)
#         if s=="0":
#             s2+='zero'
#         if s=="1":
#             s2+='one'
#         if s=="2":
#             s2+='two'
#         if s=="3":
#             s2+="three"
#         if s=="4":
#             s2+='four'
#         if s=="5":
#             s2+='five'
#         if s=="6":
#             s2+='six'
#         if s=="7":
#             s2+='seven'
#         if s=="8":
#             s2+='eight'
#         if s=="9":
#             s2+='nine'
#         s2+=" "
#     dic[v]=s2
# print(dic)

# q6
# s="jyoti rani behera "
# d={}
# c,sp=0,0
# st=""
# for s1 in s:
#     if s1==" ":
#         d[st]=c
#         sp+=1
#         d["spacel"+str(sp)]=sp
#         st,c="",0
#     else:
#         st+=s1
#         c+=1
# print(d)


    