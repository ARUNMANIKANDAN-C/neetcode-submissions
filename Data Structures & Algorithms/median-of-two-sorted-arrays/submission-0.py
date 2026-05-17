class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        m = len(nums1)
        n = len(nums2)

        if (m+n) % 2 == 1:
            out = [(m+n)//2]
        else:
            out = [(m+n)//2 - 1, (m+n)//2]

        k = 0
        l = 0
        o = []

        while k + l <= out[-1]:

            if k < m and l < n:

                if nums1[k] <= nums2[l]:

                    if k + l in out:
                        o.append(nums1[k])

                    k += 1

                else:

                    if k + l in out:
                        o.append(nums2[l])

                    l += 1

            elif k < m:

                if k + l in out:
                    o.append(nums1[k])

                k += 1

            else:

                if k + l in out:
                    o.append(nums2[l])

                l += 1

        return sum(o) / len(o)