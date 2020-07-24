class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        N = len(graph)
        ans = []
        def backtrack(node_index, path):
            if node_index == N-1:
                ans.append(path[:])
                return 
            for v in graph[node_index]:
                backtrack(v, path + [v])
        backtrack(0,[0]) 
        return ans
