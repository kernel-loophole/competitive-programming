#defining list from base class
l=list()
l.append("abc")
l.insert(1,"make")
l.append("check")
print(l)
#LIST slicing 
print(l[::1])
print(l[1:2])
print(l[1::2])
print(l[1::-1])
#find number of element in list
print(len(l))
#find max in list
print(max(l))
#Looping through List
for i in l:
    print(i)
for i in range(0,len(l)):
    print(l[i])




name_list=["mr.abc","mr.xyz","hello"]
list_herto=["hello",123,"xyz"]
list_of_number=[1,2,3,4]
# print(name_list)
# print(list_herto)
# print(list_of_number)