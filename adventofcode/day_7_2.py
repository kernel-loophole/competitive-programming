import re
def sum_the_str(list_of_checks:list,total:int):
    for j in list_of_checks:
            x=re.findall('[0-9]+',j)
            total=total+int(x[0])
            print("total size of dir",total)
def recursively_find(dir_string:str,file_content:str,total_size:int,dir_mapping:dict):
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
                dir_string=i[len(i)-2]
                # recursively_find(dir_string,file_content)
    for i in check_dir:
        for k in re.findall('[0-9]+',i):
            total_size_of_dir=total_size_of_dir+int(k)
            # print("sum",k)
    total_size=total_size+total_size_of_dir    
    if dir_string in dir_mapping:
        tmp=dir_mapping[dir_string]
        print("tmp===>",tmp)
        print("total====>",total_size)
        dir_mapping[dir_string]=tmp+total_size*2
    else:
        dir_mapping[dir_string]=total_size
    return dir_mapping
def find_dir(list_string:__file__)->str:
    total=0
    dir_mapping={}
    for i in list_string:
        try:
            if i.startswith('dir'):
                # print(i[len(i)-2])
                print("dir ")
                dir_string=i[4:len(i)]

                print(recursively_find(dir_string,list_string,total,dir_mapping))
        except:
            pass
        if i.startswith('$ cd'):
            pass
    final_output=0
    for total_sum in dir_mapping.values():
        if total_sum<100000:
            final_output=final_output+total_sum
    print(final_output)
def open_file(file_name):
    total_sum=0
    with open(file_name,'r') as f:
        plaintext=f.readlines()
    find_dir(plaintext)
if __name__=="__main__":
    open_file("day7_input.txt")
