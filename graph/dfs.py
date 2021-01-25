graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}


visited = set() # Set to keep track of visited nodes.

def dfs(visited, graph, node):
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Driver Code
dfs(visited, graph, 'A')

#if binary tree
def dfs_binary_tree(root):

       if root is None:
           return
       else:
           print(root.value,end=" ")
           dfs_binary_tree(root.left)
           dfs_binary_tree(root.right)
#connected component
def find_connected_components(graph):
       visited = []
       connected_components = []
       for node in graph.nodes:
           if node not in visited:
               cc = [] #connected component
               visited, cc = dfs_traversal(graph, node, visited, cc)
               connected_components.append(cc)
       return connected_components

   def dfs_traversal(graph, start, visited, path):
       if start in visited:
           return visited, path
       visited.append(start)
       path.append(start)
       for node in graph.neighbors(start):
           visited, path = dfs_traversal(graph, node, visited, path)
       return visited, path
        
#topological sort
        
def dfs(dag, start, visited, stack):

       if start in visited:
           # node and all its branches have been visited
           return stack, visited
       if dag.out_degree(start) == 0:
           # if leaf node, push and backtrack
           stack.append(start)
           visited.append(start)
           return stack, visited

       #traverse all the branches
       for node in dag.neighbors(start):
           if node in visited:
               continue
           stack, visited = dfs(dag, node, visited, stack)

       #now, push the node if not already visited
       if start not in visited:
           print("pushing %s"%start)
           stack.append(start)
           visited.append(start)
       return stack, visited

   def topological_sort_using_dfs(dag):
       visited = []
       stack=[]
       start_nodes = [i for i in dag.nodes if dag.in_degree(i)==0]
    #print(start_nodes)

       for s in start_nodes:
           stack, visited = dfs(dag, s, visited, stack)
       print("Topological sorted:")
       while(len(stack)!=0):
           print(stack.pop(), end=" ")