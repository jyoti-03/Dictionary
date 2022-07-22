# d1={'a':100,'b':200,'c':300}
# d2={'a':300,'b':200,'d':400}
# a={}
# for i in d1:
#     for j in d2:
#         if i in d2:
#             a[i]=d1[i]+d2[i]
#         elif j not in d1:
#             a[j]=d2[j]
#         elif i not in d2:
#             a[i]=d1[i]
# print(a)

d1={'a':100,'b':200,'c':300}
d2={'a':300,'b':200,'d':400}
counter = d1.copy()
for key in d2:
    if key in counter:
        counter[key] += d2[key]
    else:
        counter[key] = d2[key]
print(counter)