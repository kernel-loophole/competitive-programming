import re
def count_string():
    pass
total=0
def content_finder(string,content):
    dir_content=[]
    flag=False
    str="$ cd "+string
    print(str)
    for i in content:
        if i.startswith("$ cd"+string):
            dir_content.append(i)
        if i.startswith("$") and flag==True:
            break
    print(dir_content)
def dir_locator(dir,string):
    tmp_list=[]
    flag=False
    for i in string:
        if i.startswith('$ cd') and flag==True:
            break
        if flag:
            tmp_list.append(i)
        if i.startswith(dir):
            flag=True
    for i in tmp_list:
        if i.startswith('dir'):
            content_finder(i[4:5],string)
        else:
            pass

def find_dir(list_string):
    for i in list_string:
        if i.startswith('dir'):
            print(i)
        if i.startswith('$ cd'):
            
            dir_locator(i,list_string)
def open_file(file_name):
    total_sum=0
    with open(file_name,'r') as f:
        plaintext=f.readlines()
    find_dir(plaintext)
    # for i in plaintext:
    #     x=re.findall('[0-9]+',i)
    #     try:
    #         total_sum=total_sum+int(x[0])
    #     except:
    #         pass
    # print(total_sum)
if __name__=="__main__":
    open_file("day7_input.txt")
