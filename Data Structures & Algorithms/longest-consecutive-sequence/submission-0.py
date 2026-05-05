class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        count=0
        nums=sorted(nums)
        prev=nums[0]
        #dp = [0]*len(nums)
        for i in nums[1:]:
            if prev+1==i:
                if count==0:
                    count=2
                else:
                    count+=1
            prev=i
        return count 