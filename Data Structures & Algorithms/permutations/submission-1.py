class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def fun(arr):
            if len(arr) == len(nums):
                ans.append(arr.copy())
                return

            for num in nums:
                if num not in arr:
                    fun(arr + [num])

        fun([])
        return ans