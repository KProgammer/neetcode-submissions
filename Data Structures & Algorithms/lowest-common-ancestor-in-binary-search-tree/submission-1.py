# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        # if p <= root node <= q or if q <= root node <- p then I've arrived 
        # at the solution. In other words, while both of these are not true, then 
        # continue to search
        # while (not ((p.val <= root.val) and (root.val <= q.val))) and (not ((p.val >= root.val) and (root.val >= q.val))):

        #     # if p and q are < root node shift root node to the left descendant
        #     if ((p.val < root.val) and (q.val < root.val)):
        #         root = root.left
        #     # if p and q are > root node shift root node to the right descendant
        #     elif ((p.val > root.val) and (q.val > root.val)):
        #         root = root.right
        # 
        # return root
          
            # solution
            cur = root

            while cur:
                if p.val > cur.val and q.val > cur.val:
                    cur = cur.right
                elif p.val < cur.val and q.val < cur.val:
                    cur = cur.left
                else:
                    return cur
            



        