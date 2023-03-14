from collections import deque
class DLLNode :
    def __init__(self,val) -> None:
        self.next = self.prev = None
        self.val = val

class DoublyLinkedList :
    def __init__(self) -> None:
        self.dummy_head,self.dummy_tail = DLLNode(-1),DLLNode(-1)
        self.dummy_head.next,self.dummy_tail.next = self.dummy_tail,self.dummy_head
        self.dummy_head.prev,self.dummy_tail.prev = self.dummy_tail,self.dummy_head
        self.size = 0
    
    def remove_node(self,val) :
        if self.size <= 0 :
            return 
        else  :
            cur = self.dummy_head.next
            while cur != self.dummy_tail and cur.val != val :
                cur = cur.next
            if cur == self.dummy_tail :
                return
            else :
                prev,next = cur.prev,cur.next
                prev.next = cur.next
                next.prev = cur.prev
                self.size-=1
    
    def add_node_to_head(self,val) :
        new_node = DLLNode(val)
        prev,next = self.dummy_head,self.dummy_head.next
        new_node.prev,new_node.next = prev,next
        prev.next = next.prev = new_node
        self.size+=1
    
    def add_node_to_tail(self,val) : 
        new_node = DLLNode(val)
        prev,next = self.dummy_tail.prev,self.dummy_tail
        new_node.prev,new_node.next = prev,next
        prev.next = next.prev = new_node
        self.size+=1
    
    def string_of(self) :
        vals = deque()
        cur = self.dummy_head.next
        while cur != self.dummy_tail :
            vals.append(str(cur.val))
            cur = cur.next
        return "->".join(list(vals))

if __name__ == '__main__' :
    dll = DoublyLinkedList()
    dll.add_node_to_head(1)
    dll.add_node_to_head(2)
    dll.add_node_to_head(10)
    dll.add_node_to_tail(100)
    print(f"DLL is {dll.string_of()}")
    dll.remove_node(2)
    dll.remove_node(2)
    print(f"DLL is {dll.string_of()}")



