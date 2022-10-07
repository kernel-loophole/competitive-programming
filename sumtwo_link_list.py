
'''You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself. '''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        return sum_link_list(list1,list2)
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
    s=Solution()
    s.mergeTwoLists(l1,l2)