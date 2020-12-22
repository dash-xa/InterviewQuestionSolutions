class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = {} # digraph 
        for u, v, p in flights: 
            graph.setdefault(u, []).append((v, p)) 
            
        pq = [(0, -1, src)] # min-heap (cost-stop-city)
        while pq: 
            p, k, u = heappop(pq) # current stop 
            if k <= K: 
                if u == dst: return p
                for v, pp in graph.get(u, []): 
                    heappush(pq, (p + pp, k+1, v))
        return -1