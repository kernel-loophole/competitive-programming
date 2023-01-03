with open('input_data.txt','r') as file:
    content=file.readlines()
final_socre_list=[]
groups=[]
count=0
groups_score=[]
for i in content:
    left_side=i[0:len(i)//2]
    right_side=i[len(i)//2:len(i)]
    for j in left_side:
        if j in right_side:
            if j.isupper():
                # print("=======>upper",(ord(j)-64)+26)
                final_socre_list.append((ord(j)-64)+26)
            else:
                # print("lower")
                # print(ord(j)-96)
                final_socre_list.append(ord(j)-96)
            break
    groups.append(i)
    if len(groups)==3:
        list_1=list(groups[0])
        list_2=list(groups[1])
        list_3=list(groups[2])
        #part two
        for l in list_1:
            if l in list_2 and l in list_3:
                if l.isupper():
                    groups_score.append((ord(l)-64)+26)
                else:
                    groups_score.append((ord(l))-96)
                print(l)
                break


        groups=[]
print(sum(final_socre_list))
print(sum(groups_score))
