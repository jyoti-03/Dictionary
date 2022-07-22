n=int(input("how many students-: "))
d={}
for i in range(0,n):
    na=input("emter student name-: ")
    ma=int(input("enter marks-: "))
    d.update({na:ma})
print(d)
