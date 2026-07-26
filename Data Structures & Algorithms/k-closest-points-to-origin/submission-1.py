class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        l = []

        for p in points:
            dist = p[0]**2 + p[1]**2
            l.append([dist, p])

        l.sort()

        return [point for _, point in l[:k]]