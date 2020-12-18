from heapq import heappop, heappush
class Solution:
    def networkDelayTime(self, times, N, K):
        # Generate adjacency list
        adj = {i:[] for i in range(1, N + 1)}
        for fr, to, time in times:
            adj[fr].append((time, to))
        # Generate max paths tree
        shortestDistTree = {}
        q = []
        heappush(q, (0, K))
        while q:
            w, n = heappop(q)
            if n in shortestDistTree:
                continue
            shortestDistTree[n] = w
            for cost, neighbor in adj[n]:
                if neighbor not in shortestDistTree:
                    heappush(q, (cost + w, neighbor))
        return max(shortestDistTree.values()) if len(shortestDistTree) == N else -1
times = [[1,2,1],[2,1,3]]
N = 2
K = 2
sol = Solution()
assert (sol.networkDelayTime(times, N, K)) == 3

times = [[2,1,1],[2,3,1],[3,4,1]]
N = 4
K = 2
assert (sol.networkDelayTime(times, N, K)) == 2

