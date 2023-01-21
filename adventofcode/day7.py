import re
def count_string():
    pass
def open_file(file_name):
    total_sum=0
    with open(file_name,'r') as f:
        plaintext=f.readlines()
    for i in plaintext:
        x=re.findall('[0-9]+',i)
        try:
            total_sum=total_sum+int(x[0])
        except:
            pass
    print(total_sum)
if __name__=="__main__":
    open_file("day7_input.txt")
