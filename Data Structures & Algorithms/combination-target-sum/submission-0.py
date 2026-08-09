class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        ans = []

        def fun(num=0, arr=[], id=0):
            if num == target:
                ans.append(arr)
                return

            if num > target:
                return

            for i in range(id, len(nums)):
                fun(num + nums[i], arr + [nums[i]], i)

        fun()
        return ans