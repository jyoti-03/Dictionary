# s="my name is jyoti"
# ss=list(s.split())
# s2="MY NAME IS JYOTI"
# SS=s.join(s2)
# # print(ss)
# print(SS)

a={'data':{
    'jan':{'mon':3,'tues':4,'wed':3,'thurs':4,'fri':5,'sat':3,'sun':4},
    'feb':{'mon':5,'tues':5,'wed':4,'thurs':7,'fri':2,'sat':3,'sun':7},
    'march':{'mon':7,'tues':4,'wed':3,'thurs':4,'fri':5,'sat':3,'sun':4},
    'april':{'mon':8,'tues':4,'wed':3,'thurs':4,'fri':5,'sat':3,'sun':4},
    'may':{'mon':3,'tues':4,'wed':3,'thurs':4,'fri':5,'sat':3,'sun':4},
    'june':{'mon':2,'tues':4,'wed':3,'thurs':4,'fri':5,'sat':3,'sun':4},
    'july':{'mon':5,'tues':4,'wed':3,'thurs':4,'fri':5,'sat':3,'sun':4},
    'aug':{'mon':3,'tues':4,'wed':3,'thurs':4,'fri':5,'sat':3,'sun':4},
    'sep':{'mon':8,'tues':4,'wed':3,'thurs':4,'fri':5,'sat':3,'sun':4},
    'oct':{'mon':7,'tues':4,'wed':3,'thurs':4,'fri':5,'sat':3,'sun':4},
    'nov':{'mon':7,'tues':4,'wed':3,'thurs':4,'fri':5,'sat':3,'sun':4},
    'dec':{'mon':5,'tues':4,'wed':3,'thurs':4,'fri':5,'sat':3,'sun':4}}
}
sum=0
for k in a["data"]:
    for v in  a['data'][k].values():
        if v>4:
            print(v)
# print(sum)

# d={1:"one",2:"two",4:"four",5:"five"}
# d.pop(1)
# print(d)
# d.popitem()
# print(d)
# del d[4]
# print(d)
# d.clear()
# print(d)

