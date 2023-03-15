from collections import deque
class GraphAdjancyList :
    def __init__(self) -> None:
        self.edges = {}
    
    def insert_edge(self,i,j) :
        if i not in self.edges :
            self.edges[i] = set()
        if j not in self.edges :
            self.edges[j] = set()
        
        self.edges[i].add(j)
        self.edges[j].add(i)
    
    def remove_edge(self,i,j) :
        if i  in self.edges :
            self.edges[i].remove(j)
        if j in self.edges :
            self.edges[j].remove(i)
    
    def edge_exist(self,i,j) :
        return i in self.edges and j in self.edges and i in self.edges[j] and j in self.edges[i]
    
    def bfs(self,src) :
        if src not in self.edges :
            return []
        
        queue,visited = deque(),set()
        queue.append(src)
        visited.add(src)
        lvls = []

        while len(queue) > 0 :
            n = len(queue)
            cur_lvl  = []
            for _ in range(n) :
                cur_vertex = queue.popleft()
                for adj in self.edges[cur_vertex] :
                    if adj not in visited :
                        queue.append(adj)
                        visited.add(adj)
                cur_lvl.append(cur_vertex)
            lvls.append(cur_lvl)
        
        return lvls
    
    def dfs(self,src) :
        def helper(cur_vertex,visited,nodes) :
            visited.add(cur_vertex)
            for adj in self.edges[cur_vertex] :
                if adj not in visited :
                    helper(adj,visited,nodes)
            nodes.append(cur_vertex)
        
        nodes = []
        helper(src,set(),nodes)
        return nodes

                


def main():
    g = GraphAdjancyList()
    g.insert_edge(0,1)
    g.insert_edge(0,3)
    g.insert_edge(1,2)
    bfs_lvls = g.bfs(0)
    dfs_nodes = g.dfs(0)
    print(f"BFS for g is {bfs_lvls}")
    print(f"DFS for g is {dfs_nodes}")


if __name__ == '__main__' :
    main()