def open_file(file_name):
    total_sum=0
    with open(file_name,'r') as f:
        plaintext=f.readlines()
    return plaintext
def finding_top(file_text:str):
    top_layer_content=file_text[0]
    print(top_layer_content[1:len(file_text)-1])
def findig_bottom(file_text:str):
    print()
    top_layer_content=file_text[len(file_text)-1]
    print(top_layer_content[1:len(file_text)-1])
def findig_right(file_text:str):
    x= ([i[0] for i in file_text ])
    print("right",x)
def findig_left(file_text:str):
    x= ([i[len(i)-2] for i in file_text ])
    print("left",x)
def main():
    file_content=open_file('day8.txt')
    finding_top(file_content)
    findig_bottom(file_content)
    findig_left(file_content)
    findig_right(file_content)
if __name__=="__main__":
    main()