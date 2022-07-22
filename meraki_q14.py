d={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
# d={1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
li=list(d.values())
r=list(d.values())
li.sort()
x={}
for i in li:
    for j in d:
        if d[j] == i:
            x[j]=i
print(x)
#{'param':20,'anjili':30,'bijender':45,'roshini':50,'deepak':60}
#Ascending

r.sort(reverse=True)
y={}
for k in r:
    for l in d:
        if d[l] == k:
            y[l]=k
print(y)

# #{'deepak':60,'roshini':50,'bijender':45,'anjili':30,'param':20}
#Descending

