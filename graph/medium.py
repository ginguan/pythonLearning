#277. Find the Celebrity

# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

def findCelebrity(self, n):
    """
    :type n: int
    :rtype: int
    """
    self.n = n
    for i in range(n):
        if(self.is_Celebrity(i)):
            return i
    return -1

def is_Celebrity(self,person):
    for other in range(self.n):
        if person==other:continue
        if knows(person,other) or not knows(other,person):
            return False
    return True

def findCelebrity(self, n):
    x = 0
    for i in range(n):
        if knows(x, i):
            x = i
    if any(knows(x, i) for i in range(x)):
        return -1
    if any(not knows(i, x) for i in range(n)):
        return -1
    return x


# 797 All Paths From Source to Target
def allPathsSourceTarget(self, graph):
    """
    :type graph: List[List[int]]
    :rtype: List[List[int]]
    """
    res =[]
    part=[]
    def findOne(node):
        if node == len(graph)-1:
            res.append(part[:])
            return
        for i in graph[node]:
            part.append(i)
            findOne(i)
            part.pop()
    part.append(0)
    findOne(0)
    return res

#841. Keys and Rooms
def canVisitAllRooms(self, rooms):
    visited = [False] * len(rooms)
    visited[0] = True
    stack = [0]
    #At the beginning, we have a todo list "stack" of keys to use.
    #'visited' represents at some point we have entered this room.
    while stack:  #While we have keys...
        key = stack.pop() # get the next key
        for nei in rooms[key]: # For every key in room # 'key'...
            if not visited[nei]: # ... that hasn't been used yet
                visited[nei] = True # mark that we've entered the room
                stack.append(nei) # add the key to the todo list
    return all(visited) # Return true iff we've visited every room

#1302. Deepest Leaves Sum
def deepestLeavesSum(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    #level = 0
    levels=[]
    def df_node(root,level):
        if root is None:
            return
        else: 
            level+=1
            levels.append([root.val,level])
            df_node(root.left,level)
            df_node(root.right,level)
    df_node(root,0)
    new_list = sorted(levels, key=lambda x: x[1])
    res = 0
    print(new_list)
    for i,j in new_list:
        if j == new_list[-1][1]:
            res+= i
    return res

def deepestLeavesSum(self, root):
    # Initialization:
    # prev level as empty list
    # traversal queue as root node
    prev_level, traversal_queue = [],  [ root ]

    # Level-order-traversal
    while traversal_queue:

        # update previous level as current traversal queue 
        # update current traversal queue as next level queue

        prev_level, traversal_queue = traversal_queue, [ leaf for node in traversal_queue for leaf in (node.left, node.right) if leaf ]


    # When the level-order-traversal is completed,
    # prev_level contains those nodes in deepest level

    return sum( node.val for node in prev_level if node )


#1557
def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:

    res =[]
    degree = {}
    for node in range(n):
        degree[node]=0
    for a,b in edges:
        degree[b]+=1
    print(degree)
    for node in degree:
        if degree[node]==0:
            res.append(node)
    return res

#using dfs
def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
    def dfs(g,c,vis,res):
        vis[c] = True
        for adj in g[c]:
            if not vis[adj]:
                dfs(g,adj,vis,res)
            #adj can be visited by current vertex so we dont have to add adj in res
            elif adj in res:res.remove(adj)

    #Make a adjecency list
    g = collections.defaultdict(list)
    for e in edges:
        u,v = e
        g[u].append(v)


    res = set()
    vis = [False]*n
    for i in range(n):
        if not vis[i]:
            dfs(g,i,vis,res)
            #add vertex from which we start traversing
            res.add(i)
    return list(res)


#1615. Maximal Network Rank

