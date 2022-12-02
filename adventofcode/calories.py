with open('calories.txt','r') as f:
    x=f.readlines()
    # for i in f.readline():
    #     print(i)
    count=0
    adding_list=[]

    for i in x:
        if i=='\n':
            adding_list.append(count)
            count=0
            continue
        count=count+int(i)
    print(adding_list)
    #====================part 1==============
# print(max(adding_list))
#==============part 2============
#check it =============
adding_list=sorted(adding_list,reverse=True)
print(sum(adding_list[0:3]))
# 73211
