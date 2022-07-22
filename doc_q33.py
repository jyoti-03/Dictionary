dict={'alex':{'class':'v','roll_id':2},'puja':{'class':'v','roll_id':3}}
for i in dict:
    # print(i)
    for j in dict[i]:
        print(j,':',dict[i][j])
    print()
