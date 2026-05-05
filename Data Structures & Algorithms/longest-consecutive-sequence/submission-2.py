class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)>=2:
            count=1
            nums=sorted(nums)
            prev=nums[0]
            #dp = [0]*len(nums)
            for i in nums[1:]:
                if prev+1==i:
                    count+=1
                prev=i
            return count 
        elif len(nums)==1:
            return 1
        else:
            return 0