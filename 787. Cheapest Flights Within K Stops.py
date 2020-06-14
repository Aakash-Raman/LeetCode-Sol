class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], s: int, d: int, k: int) -> int:
        graph = collections.defaultdict(list)
        
        for u, v, c in flights:
            graph[u].append((v, c))
        
        queue = collections.deque([(s, 0, 0)])
        minCost = float('inf')
        
        while queue:
            node, stops, costsoFar = queue.popleft()
            
            if node == d:
                minCost = min(minCost, costsoFar)
                continue
            
            if stops > k or costsoFar > minCost:
                continue
            
            for nei, nc in graph[node]:
                queue.append((nei, stops + 1, costsoFar + nc))
        
        return minCost if minCost != float('inf') else -1 
