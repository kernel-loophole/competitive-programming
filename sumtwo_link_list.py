'''sum the link list '''
def sum_list(l):
    final_number=''
    for i in l:
        final_number=final_number+str(i)
    return final_number


def sum_link_list(l1,l2):
    l_1=l1[::-1]
    l_2=l2[::-1]
    final_str=int(sum_list(l_1))+int(sum_list(l_2))
    final_list=list(str(final_str))
    final_list=final_list[::-1]
    for i in range(0,len(final_list)):
        final_list[i]=int(final_list[i])
    print(final_list)

if __name__=="__main__":
    l1=[3,2,1]
    l2=[6,5,4]
    sum_link_list(l1,l2)
