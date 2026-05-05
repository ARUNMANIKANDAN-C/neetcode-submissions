class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        kp=0
        left_product=1
        mp=1
        for j in nums:
            left_product*=j
            for i in nums[1:]:
                mp=mp*i
            nums[kp]=left_product*mp
            kp+=1
        return nums