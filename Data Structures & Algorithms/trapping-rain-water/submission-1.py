from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
            
        l = 0
        r = len(height) - 1

        lm = 0  
        rm = 0  
        water = 0
        
        while l < r:
            if height[l] < height[r]:
                if height[l] >= lm:
                    lm = height[l]
                else:
                    water += lm - height[l]  
                l += 1
            else:
                if height[r] >= rm:
                    rm = height[r]  
                else:
                    water += rm - height[r]  
                r -= 1
        return water