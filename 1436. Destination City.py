class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        left = []
        for i in range(0,len(paths)):
            left.append(paths[i][0])
        right = []
        for i in range(0,len(paths)):
            right.append(paths[i][1])
        left.sort()
        right.sort()
        for i in right:
            f = 0
            for j in left:
                if(j == i):
                    f = 1
            if(f == 0):
                return i
