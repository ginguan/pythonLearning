def findJudge(self, N, trust):
    """
    :type N: int
    :type trust: List[List[int]]
    :rtype: int
    """

    if len(trust)<N-1:
        return -1

    a = set()
    b = set()
    noTrust = dict()
    for j,k in trust:
        b.add(j)
    for i in range(N):
        a.add(i+1)
        if not i+1 in b:
            noTrust[i+1]=0

    for t,n in trust:
        if n in noTrust:
            noTrust[n]+=1
    for x in noTrust.keys():
        if noTrust[x]==N-1:
            return x
    return -1

#589  N-ary Tree Preorder Traversal
def preorder(self, root):
    """
    :type root: Node
    :rtype: List[int]
    """
    if not root:
        return []

    else:
        # general case:

        path = []

        # Travese current node with preorder:
        path.append( root.val )

        # Traverse children with preorder:
        for child in root.children:
            path += self.preorder( child )

        return path
    
#iterative
def preorder(self, root: 'Node') -> List[int]:

    # base_case:
    traverse_stack = [root]
    path = []

    # general case:
    while traverse_stack:

        current = traverse_stack.pop()

        if current:

            # Travese current node with preorder:
            path.append( current.val )


            if not current.children:
                continue


            # Traverse children with preorder:
            # Left part if of higher priority than right part.
            # Thus, push right part before left part.
            for i in range( len(current.children)-1, -1, -1 ):
                traverse_stack.append( current.children[i] )

    return path