class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s= set(numbers)
        l = []
        for i in s:
            if i-taarget in l:
                return [l,i]
            l.append(i)