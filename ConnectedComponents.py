# DFS solution in O(n+e)
# Can there be any number of connected components, from 1 to n?
# Are values of each node unique?
# Can a node point to itself?

# Input: file
# First n and e. n=number of nodes, e is number of edges
# Then list of edges follows
# 1. Generate adjacency list
    # seen = [False] * n
# 2. For each node i in 1..n:
#       if not seen[n]
#       Run dfs to get connected components, keeeping track of which nodes we've seen
def parseInputLine():
    return map(int, input().split(" "))

def parseEdges(e):
    edges = []
    for _ in range(e):
        edges.append(parseInputLine())
    return edges

def buildAdjacencyList(n, edges):
    adj = [[] for _ in range(n+1)]
    for fr, to in edges:
        adj[fr].append(to)
        adj[to].append(fr)
    return adj

def markComponent(node, adj, seen):
    seen[node] = True
    for child in adj[node]:
        if not seen[child]:
            markComponent(child, adj, seen)
        
def countComponents(n, edges):
    adj = buildAdjacencyList(n, edges)
    seen = [False] * (n+1)
    numComponents = 0
    for i in range(1, n+1):
        if not seen[i]:
            markComponent(i, adj, seen)
            numComponents += 1
    return numComponents

def getNumConnectedComponents():
    n, e = parseInputLine()
    edges = parseEdges(e)
    return countComponents(n, edges)

print(getNumConnectedComponents())

# Mistakes: 
# Mistook undirected for directed graph when parsing edge inputs
# if node not in seen vs if child not in seen