# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import copy
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # the idea is to follow the pattern 0, n-1, 1, n-2, 2, ... and so on by arranging the linked list
        
        # lst = []
        # cur_node = head
        # # copy over every element
        # while (cur_node):
        #     lst.append(cur_node)
        #     cur_node = cur_node.next

        # # copy over elements
        # cur_node = head
        # lst_len = len(lst)
        # # print("DEBUG:lst_len =",lst_len)
        # ind = 1
        # counter = 1
        # while(counter < lst_len):  
        #     if((-1)**(counter) < 0):  
        #         cur_node.next = lst[int(lst_len-(ind//1))]
        #         # print("DEBUG:lst[lst_len-(ind//1)]")
        #     else:
        #         cur_node.next = lst[int(ind//1)]
        #         # print("DEBUG:lst[ind//1]")
        #     cur_node = cur_node.next     
        #     ind += 0.5
        #     counter += 1
        #     # print("DEBUG:counter =",counter)
        
        # cur_node.next = None


        # Solution
        slow,fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        prev = slow.next = None

        # reverse two halfs
        while second:
            tmp = second.next
            second.next = prev
            prev = second 
            second = tmp

        # merge two halfs
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2


       