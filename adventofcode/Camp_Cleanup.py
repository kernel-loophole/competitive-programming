with  open('camp_cleanup.txt','r') as file:
    content=file.readlines()
total_count=0
def check_out(list1,list2)->list:
    if list1 in list2  or list2 in list1:
        return True
    return False
def make_list(list1,list2)->"two lists with number":
    tmp_list=''
    tmp_list_2=''
    for i in list1:
        tmp_list=tmp_list+str(i)
    for j in list2:
        tmp_list_2=tmp_list_2+str(j)
    return tmp_list,tmp_list_2
for i in content:
    number=''
    number2=''
    flag=True
    comma_flag=True
    for j in i:
        if j==',':
            number=int(number)
            number2=abs(int(number2))
            tmp_list_1=list(range(number,number2+1))
            number=''
            number2=''
            comma_flag=False
            flag=True
        if j=='-':
            flag=False
        if flag:
            if j!=",":
                number=number+str(j)
        if not flag:
            if j!=",":
                number2=number2+str(j)
    tmp_list_2=list(range(int(number),abs(int(number2))+1))
    x,y=make_list(tmp_list_1,tmp_list_2)
    if check_out(x,y):
        total_count+=1
print(total_count)
