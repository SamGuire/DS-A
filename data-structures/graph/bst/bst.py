from collections import deque
class TreeNode :
    def __init__(self,val) -> None:
        self.left = self.right = self.parent = None
        self.val = val

class BinarySearchTree :
    def __init__(self) -> None:
        self.root = None

    def insert(self,val) :
        new_node = TreeNode(val)
        if not self.root :
            self.root = new_node
            return
        else :
            p,c = None,self.root
            while c :
                if c.val == val :
                    return
                elif val > c.val :
                    p,c = c,c.right
                else :
                    p,c = c,c.left
            if val > p.val :
                p.right = new_node
            else :
                p.left = new_node
            new_node.parent = p
    
    def remove(self,val) :
        def remove_recursive(cur_node,val) :
            if not cur_node :
                return 
            elif val > cur_node.val :
                cur_node.right = remove_recursive(cur_node.right,val)
                return cur_node
            elif val < cur_node.val :
                cur_node.left = remove_recursive(cur_node.left,val)
                return cur_node
            else :
                if cur_node.left and cur_node.right :
                    successor_node = self.get_successor(cur_node)
                    cur_node.val = successor_node.val
                    cur_node.right = remove_recursive(cur_node.right,successor_node.val)
                    return cur_node
                elif cur_node.left :
                    return cur_node.left
                else :
                    return cur_node.right
        
        remove_recursive(self.root,val)

    def get_min(self,node) :
        cur_node = node
        while cur_node.left :
            cur_node = cur_node.left
        return cur_node
    
    def get_max(self,node) :
        cur_node = node
        while cur_node.right :
            cur_node = cur_node.right
        return cur_node
    
    def get_successor(self,node) :
        if node.right :
            return self.get_min(node.right)
        else :
            p,c = node.parent,node
            while p :
                if p.left == c :
                    return p
                else :
                    c = p
                    p = p.parent
            return None
    
    def get_predecessor(self,node) :
        if node.left :
            return self.get_max(node.left)
        else :
            p,c = node.parent,c
            while p :
                if p.right == c :
                    return p
                else :
                    c = p
                    p = p.parent
            return None
    
    def inorder(self) :
        stack = deque()
        res = deque()
        c= self.root
        while c or len(stack) > 0 :
            while c :
                stack.append(c)
                c = c.left
            tmp = stack.pop()
            res.append(tmp.val)
            c = tmp.right
        return res
    
    def preorder(self) :
        if not self.root :
            return []
        stack = deque()
        res = deque()
        stack.append(self.root)
        while len(stack) > 0 :
            c = stack.pop()
            res.append(c.val)
            if c.right :
                stack.append(c.right)
            if c.left :
                stack.append(c.left)
        
        return res
    
    def postorder(self) :
        if not self.root :
            return []
        stack = deque()
        res = deque()
        stack.append(self.root)
        while len(stack) > 0 :
            c = stack.pop()
            res.append(c.val)
            if c.left :
                stack.append(c.left)
            if c.right :
                stack.append(c.right)
        return list(res)[::-1]




def main():
    bst = BinarySearchTree()
    bst.insert(1)
    bst.insert(2)
    bst.insert(3)
    bst.insert(0)
    print(f"inorder of bst is {bst.inorder()}")
    bst.remove(1)
    print(f"inorder of bst is {bst.inorder()}")


if __name__ == '__main__' :
    main()