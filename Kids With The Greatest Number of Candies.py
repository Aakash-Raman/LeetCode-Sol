class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)
        final = []
        for i in candies:
            if(i + extraCandies >= maxCandies):
                final.append(True)
            else:
                final.append(False)
        return final
