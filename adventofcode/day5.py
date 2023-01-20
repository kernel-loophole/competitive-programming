with open("day5.txt") as f:
    counter=1
    reverse_file=f.readlines()
    reverse_file=reverse_file[::-1]
    tmp_list=[]
    flag=False
    for i in reverse_file:
        if flag:
            for j in i:
                if j=='[' or j==']':
                    pass
                else:
                    l_1=[]
                    l_1.append(j)
                    tmp_list.append(l_1)
            print(i)
        try :
            if i[1]=='1':
                flag=True
        except:
            pass
print(tmp_list)
def test_fun(list_items):
    for i in list_items:
        print(i)
def mapping_list(list_items):
    counter=0
    for k in list_items:
        string=""
        try:
            for i in range(0,len(k)):
                for j in list_items:
                    string=string+j[i]
        except:
            pass
        print(string)
tmp_str=[]
final_list=[]
for key in tmp_list:
    if key[0]=='#':
        pass
    else:
        tmp_str.append(key[0])
    if key[0]=="\n":
        final_list.append(tmp_str)
        tmp_str=[]
test_fun(final_list)
mapping_list(final_list)
