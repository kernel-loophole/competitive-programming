def open_file(file_name):
    total_sum=0
    with open(file_name,'r') as f:
        plaintext=f.readlines()
    return plaintext
def finding_top(file_text:str):
    top_layer_content=file_text[0]
    return len(top_layer_content[1:len(file_text)-1])
def findig_bottom(file_text:str):
    top_layer_content=file_text[len(file_text)-1]
    return  len(top_layer_content[1:len(file_text)-1])
def findig_right(file_text:str):
    x= ([i[0] for i in file_text ])
    return len(x)
def findig_left(file_text:str):
    x= ([i[len(i)-2] for i in file_text ])
    return len(x)
def finding_values(index:int,value:int,file_content:str,count:int):
    try:
        x=file_content[index]
    except:
        pass
    for k in range(0,len(x)):
        count_flag=True
        print("comparing",x[k],"with")
        print("get the value",x[k])
        for i in file_content:
            if x[k]<i[index]:
                print("exit","row_number","index",index,x,x[k],i[index])
                count_flag=False
                break
        if count_flag:
            count=count+1
    return count
def find_sub_matrix(file_content:str):
    count=0
    count_total=0
    for i in range(1,len(file_content)-1):
        count_total=count_total+finding_values(i,file_content[i],file_content,count)
    return count_total            
def main():
    file_content=open_file('day8.txt')
    top=finding_top(file_content)
    bottom=findig_bottom(file_content)
    left=findig_left(file_content)
    right=findig_right(file_content)
    sub=find_sub_matrix(file_content)
    total=top+bottom+right+left+sub
    print(total)
if __name__=="__main__":
    main()