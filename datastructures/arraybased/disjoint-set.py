class SetNode :
    def __init__(self,id) -> None:
        self.parent = self
        self.id = id
        self.size =  1

class DisjointSet :
    def __init__(self) -> None:
        self.sets = {}
    def insert_new_set(self,i) :
        if i not in self.sets :
            self.sets[i] = SetNode(i)
    def find(self,i) :
        if i in self.sets :
            c = self.sets[i]
            while c.parent.id != c.id :
                c =  c.parent
            return c
        else :
            return None
    def merge(self,i,j) :
        if i in self.sets and j in self.sets :
            p_i,p_j = self.find(i),self.find(j)
            if p_i.size > p_j.size :
                p_j.parent = p_i
                p_i.size += p_j.size
            else :
                p_i.parent = p_j
                p_j.size += p_i.size

def main() :
    ds = DisjointSet()
    ds.insert_new_set(1)
    ds.insert_new_set(2)
    ds.insert_new_set(3)
    print(f"Parent of 1 is {ds.find(1).id}")
    ds.merge(2,3)
    ds.merge(2,1)

if __name__ == '__main__' :
    main()