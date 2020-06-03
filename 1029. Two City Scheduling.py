class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs = sorted(costs, key = lambda x:x[0] - x[1])
        price = 0
        for i in range(len(costs)):
            if i < int(len(costs)/2):
                price += costs[i][0]
            else:
                price += costs[i][1]
        print(costs)
        return price
