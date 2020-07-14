class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        
        deg_of_hour = hour * (360 / 12) % 360 + 30 * (minutes / 60)
        deg_of_min = minutes * ( 360 / 60 )
        
        max_degree, min_degree = max(deg_of_hour, deg_of_min), min(deg_of_hour, deg_of_min)
        diff = min(max_degree - min_degree, 360 + min_degree - max_degree)
        
        return diff
