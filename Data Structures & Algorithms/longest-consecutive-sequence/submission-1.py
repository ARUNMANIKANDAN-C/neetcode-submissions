class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)>2:
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
        elif len(nums)==1:
            return 1
        else:
            return 0