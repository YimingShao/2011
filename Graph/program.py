def main():
    graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])
             }

    my_set = DFS(graph, 'A', marked=None)
    print(my_set)
    my_set = BFS(graph, 'A')
    print(my_set)

def DFS(G, u, marked=None):
    if marked is None:
        marked = set()
    marked.add(u)
    for e in G[u] - marked:
        DFS(G, e, marked)
    return marked

def BFS(graph, start):
   explored = []
   queue = [start]

   while queue:
       node = queue.pop(0)
       if node not in explored:
           explored.append(node)
           neighbours = graph[node]

           for neighbour in neighbours:
               queue.append(neighbour)
   return explored




if __name__ == '__main__':
    main()