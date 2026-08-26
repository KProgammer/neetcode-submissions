class TreeNode:
    def __init__(self,val = None,left = None,right = None):
        self.val = val
        self.left = left
        self.right = right

class PrefixTree:

    def __init__(self):
        self.root = TreeNode()
        self.empty = True

    def insert(self, word: str) -> None:
        # print("DEBUG: self.root =",self.root)
        cur_node = self.root
        prev_node = cur_node

        # If the tree is empty, just fill out the root node
        if self.empty:
            cur_node.val = word
            self.empty = False
            return None

        while cur_node:
            prev_node = cur_node
            if word == cur_node.val:
                return None
            elif word < cur_node.val:
                cur_node = cur_node.left
            else:
                cur_node = cur_node.right
        
        if word < prev_node.val:
            prev_node.left = TreeNode(word)
        elif word > prev_node.val:
            prev_node.right = TreeNode(word)


    def search(self, word: str) -> bool:
        print("DEBUG:word =",word)
        # print("DEBUG:self.empty =",self.empty)
        if self.empty:
            return False
        cur_node = self.root
        while cur_node:
            # print("DEBUG:cur_node.val =",cur_node.val)
            # print("DEBUG: word == cur_node",word == cur_node)
            if word == cur_node.val:
                return True
            elif word < cur_node.val:
                cur_node = cur_node.left
            else:
                cur_node = cur_node.right
            
        return False

    def startsWith(self, prefix: str) -> bool:
        cur_node = self.root

        # if the tree is empty return false
        if self.empty:
            return False
        # else:
        while cur_node:
            if (len(prefix) <= len(cur_node.val)) and \
            (prefix == cur_node.val[:len(prefix)]):
                return True
            else:
                if prefix < cur_node.val:
                    cur_node = cur_node.left
                else:
                    cur_node = cur_node.right
        return False
        

# thoughts:
# have a set contain all the words2\

# what if I had a tree organized alphabetically and then just compare the first two letters. 