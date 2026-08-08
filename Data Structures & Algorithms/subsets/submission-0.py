class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        ans = []

        def fun(arr=[], id=0):

            if id == len(nums):
                return None

            # Take nums[id]
            fun(arr + [nums[id]], id + 1)
            ans.append(arr + [nums[id]])
            # Don't take nums[id]
            fun(arr, id + 1)

        fun()
        ans.append([])
        return ans