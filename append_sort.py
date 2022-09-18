def doc_str():
    return'''We have a list of integers X1,X2,…,XN. We would like them to be in strictly increasing order, 
    but unfortunately, we cannot reorder them. 
    This means that usual sorting algorithms will not work.

Our only option is to change them by appending 
digits 0 through 9 to their right (in base 10). 
For example, if one of the integers is 10, you can turn 
it into 100 or 109 with a single append operation, or into 
1034 with two operations (as seen in the image below).
    '''

list_of_numbers=[100,7,10,10]
counter=0
print(doc_str())
#main algo
for i in range(0,len(list_of_numbers)):
    try:
        if list_of_numbers[0]>list_of_numbers[i+1]:
            # print(list_of_numbers[i])
            tmp_str=str(list_of_numbers[i+1])
            while True:
                tmp_str=tmp_str+"9"
                counter+=1
                if int(tmp_str)>list_of_numbers[i]:
                    # print(tmp_str,counter)
                    break
            
        else:
            pass
    except:
        pass
print("total digit ==== ><=====",counter)