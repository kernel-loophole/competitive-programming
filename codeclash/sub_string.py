def sub_string(string,k):
    final_list=[]
    for i in range(0,len(string)):
        tmp_string=string[i]
        for j in range(i,len(string)):
            if len(tmp_string)==k:
                # print(tmp_string)
                final_list.append(tmp_string)
                tmp_string=string[i]
            try:
                tmp_string=tmp_string+string[j+1]
            except:
                # print('PASSING INDEX',j)
                pass
    for i in final_list:
        print(i)

sub_string("hello",2)
