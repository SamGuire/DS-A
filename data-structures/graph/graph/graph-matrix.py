from collections import deque
class GraphMatrix :
    def __init__(self,num_of_vertices) -> None:
        self.graph = [[0 for _ in range(num_of_vertices)] for _ in range(num_of_vertices)]
        self.num_of_vertices = num_of_vertices
    
    def insert(self,v_i,v_j) :
        if v_i >= self.num_of_vertices or v_j >= self.num_of_vertices or v_i < 0 or v_j < 0 :
            return
        else :
            self.graph[v_i][v_j] = 1
            self.graph[v_j][v_i] = 1
    
    def remove(self,v_i,v_j) :
        if v_i >= self.num_of_vertices or v_j >= self.num_of_vertices or v_i < 0 or v_j < 0 :
            return
        else :
            self.graph[v_i][v_j] = 0
            self.graph[v_j][v_i] = 0
    def edge_exist(self,v_i,v_j) :
        if v_i >= self.num_of_vertices or v_j >= self.num_of_vertices or v_i < 0 or v_j < 0 :
            return False
        else :
            return self.graph[v_i][v_j]  == 1 and self.graph[v_j][v_i] == 1
    
    def bfs(self,src) :
        if src >= self.num_of_vertices or src < 0 :
            return []
        queue = deque()
        lvls = deque()
        queue.append(src)
        visited = set()
        visited.add(src)
        while len(queue) >  0 :
            n = len(queue)
            new_lvl = deque()
            for _ in range(n) :
                v = queue.popleft()
                for potential_adjacent_vertex in range(self.num_of_vertices) :
                    if self.graph[v][potential_adjacent_vertex] == 1 and potential_adjacent_vertex not in visited :
                        queue.append(potential_adjacent_vertex)
                        visited.add(potential_adjacent_vertex)
                new_lvl.append(v)
            lvls.append(new_lvl)
        return lvls
    
    def dfs(self,src) :
        def helper(c_v,visited,nodes) :
            visited.add(c_v)
            for potential_adjacent_vertex in range(self.num_of_vertices) :
                if self.graph[c_v][potential_adjacent_vertex] == 1 and potential_adjacent_vertex not in visited :
                    helper(potential_adjacent_vertex,visited,nodes)
            nodes.append(c_v)
        
        if src >= self.num_of_vertices or src < 0 :
            return []
        
        nodes = []
        helper(src,set(),nodes)
        return nodes

                


def main():
    g = GraphMatrix(4)
    g.insert(0,1)
    g.insert(0,3)
    g.insert(1,2)
    bfs_lvls = g.bfs(0)
    dfs_nodes = g.dfs(0)
    print(f"BFS for g is {bfs_lvls}")
    print(f"DFS for g is {dfs_nodes}")


if __name__ == '__main__' :
    main()