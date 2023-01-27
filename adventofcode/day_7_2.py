import re
def sum_the_str(list_of_checks:list,total:int):
    for j in list_of_checks:
            x=re.findall('[0-9]+',j)
            total=total+int(x[0])
            print("total size of dir",total)
def recursively_find(dir_string:str,file_content:str,total_size:int):
    print("finding the ",dir_string)
    check_dir=[]
    str_check=''
    flag=False
    total_size_of_dir=0
    for i in file_content:
        if flag:
            check_dir.append(i)
            str_check=str_check+i
        if flag and i.startswith('$ cd '):
            if flag==False:
                flag=True
            else:
                flag=False
        if i.startswith('$ cd '+dir_string):
            # print("find====>",i)
            if flag==False:
                flag=True
            else:
                flag=False
    print(check_dir)
    
    if 'dir' in str_check:
        for i in check_dir:
            if i.startswith('dir'):
                # print("check find")
                dir_string=i[len(i)-2]
                recursively_find(dir_string,file_content)
    for i in check_dir:
        for k in re.findall('[0-9]+',i):
            total_size_of_dir=total_size_of_dir+int(k)
            print("sum",k)
    total_size=total_size+total_size_of_dir
    return total_size
def find_dir(list_string:__file__)->str:
    total=0
    for i in list_string:
        try:
            if i.startswith('dir'):
                # print(i[len(i)-2])
                dir_string=i[len(i)-2]
                print(recursively_find(dir_string,list_string,total))
        except:
            pass
        if i.startswith('$ cd'):
            pass
def open_file(file_name):
    total_sum=0
    with open(file_name,'r') as f:
        plaintext=f.readlines()
    find_dir(plaintext)
if __name__=="__main__":
    open_file("day7_input.txt")
