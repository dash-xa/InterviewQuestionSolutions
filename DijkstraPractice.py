class Solution:
    def makeAdj(self, n, edges):
        adj = [[] for i in range(n)]
        for edge in edges:
            fr, to, cost = edge
            adj[fr].append((to, cost))
        return adj
    def findCheapestPrice(self, N, flights, src, dst, K):
        adj = self.makeAdj(N, flights)
        q = [src]
        visited = [False] * N
        paths = {i:set() for i in range(N)}
        paths[src].add((0, -1))

        while q:
        	n = q.pop(0)
        	if visited[n]:
        		continue
        	visited[n] = True
        	for neighbor, w in adj[n]:
        		q.append(neighbor)
        		for cost, k in paths[n]:
        			paths[neighbor].add((cost + w, k + 1))
        print(paths[2])
        costs = [path[0] for path in paths[dst] if path[1] <= K]
        return -1 if not costs else min(costs)
sol = Solution()
# N = 3
# edges = [[0,1,100],[1,2,100],[0,2,500]]
# src = 0
# dst = 2
# k = 1
# print(sol.findCheapestPrice(N, edges, src, dst, k))

# n = 3
# edges = [[0,1,100],[1,2,100],[0,2,500]]
# src = 0
# dst = 2
# k = 0
# print(sol.findCheapestPrice(N, edges, src, dst, k))

# N = 5
# edges = [[4,1,1],[1,2,3],[0,3,2],[0,4,10],[3,1,1],[1,4,3]]
# src = 2
# dst = 1
# k = 1
# print(sol.findCheapestPrice(N, edges, src, dst, k))

N = 5
edges = [[0,1,100],[0,2,100],[0,3,10],[1,2,100],[1,4,10],[2,1,10],[2,3,100],[2,4,100],[3,2,10],[3,4,100]]
src = 0
dst = 4
k = 3
print(sol.findCheapestPrice(N, edges, src, dst, k))