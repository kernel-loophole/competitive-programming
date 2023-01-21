import re
def count_string():
    pass
total=0
def content_finder(string,content):
    dir_content=[]
    for i in content:
        if i.startswith(string):
            dir_content.append(i)
        if i.startswith("$"):
            break
    print(content)

def dir_locator(dir,string):
    tmp_list=[]
    dir_count=""
    flag=False
    for i in string:
        if i.startswith('$ cd') and flag==True:
            break
        if flag:
            if i.startswith("dir"):
                content_finder(i,string)
            else:
                tmp_list.append(i)
        if i.startswith(dir):
            flag=True

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
