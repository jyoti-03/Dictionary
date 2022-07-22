d={'a':8,'b':23,'c':45,'d':67,'e':55,'f':3}
# d={"Jyoti":5,"Rani":4,"Behera":6}
li=[]
for l in d.values():
    li.append(l)
max=0
min=0
m=li[0]
for i in li:
    if i>m:
        m=i
        max=m
    if i<m:
        min=i
print("small-",min)
print("big-",max)
