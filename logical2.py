s="My name is jyoti and jyoti is a student"
b=s.split()
# print(b)
print(s)
n=input("Enter a word from this sring-: ")
# c=b.count(n)
# print(c)

c=0
for l in b:
    if n == l:
        c+=1
print(c)
