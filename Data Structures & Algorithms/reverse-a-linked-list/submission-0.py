# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # node1->node2->node3->node4->None
        # 
        # initialize prev_node = None, cur_node=node1, and next_node=none
        # 1. Look at cur_node (node1)
        # 2. update next_node
        # 3. set cur_node's next to prev_node
        # 4. update prev_node to cur_node
        # 5. Have cur_node become the next node
        # 6. Repeat until cur_node = None
        # 7. return prev_node which should be the next_node

        prev_node = None
        cur_node = head 
        next_node = None

        while cur_node:
            next_node = cur_node.next
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = next_node

        return prev_node