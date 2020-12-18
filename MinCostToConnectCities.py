
def connected(union, a, b):
    return union[a] == union[b]
def connect(union, a, b):
    oldVal, newVal = union[a], union[b]
    for i in range(len(union)):
        if union[i] == oldVal:
            union[i] = newVal

def minCost(N, edges, newEdges):
    # Idea:
    # 1) Push newEdges onto heap
    # 2) Grow MST via Kruskal's algorithm
    # 3) Check for connectivity of components using quick find
    union = list(range(N + 1))
    for fr, to in edges:
        connect(union, fr, to)
    q = []
    for fr, to, cost in newEdges:
        heappush(q, (cost, fr, to))
    numEdges = len(edges)
    totalCost = 0
    while numEdges < N - 1:
        cost, fr, to = heappop(q)
        if not connected(union, fr, to): # add edge
            connect(union, fr, to)
            totalCost += cost 
            numEdges += 1
    return totalCost

n = 6
edges = [[1, 4], [4, 5], [2, 3]]
newEdges = [[1, 2, 5], [1, 3, 10], [1, 6, 2], [5, 6, 5]]
print(minCost(n, edges, newEdges))