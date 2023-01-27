def recursively_find(dir_string:str,file_content:str):
    check_dir=[]
    flag=False
    for i in file_content:
        if flag:
            check_dir.append(i)
        if flag and i.startswith('$ cd '):
            if flag==False:
                flag=True
            else:
                flag=False
        if i.startswith('$ cd '+dir_string):
            print("find====>",i)
            if flag==False:
                flag=True
            else:
                flag=False          
def find_dir(list_string:__file__)->str:
    for i in list_string:
        try:
            if i.startswith('dir'):
                # print(i[len(i)-2])
                dir_string=i[len(i)-2]
                recursively_find(dir_string,list_string)
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
