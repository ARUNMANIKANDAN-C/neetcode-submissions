class Solution:
    def search(self, nums, target):
        l, r = 0, len(nums) - 1

        step = 0

        while l <= r:
            mid = (l + r) // 2
            # FOUND
            if nums[mid] == target:
                return mid

            # LEFT HALF SORTED
            left_sorted = nums[l] <= nums[mid]
            if left_sorted:

                in_left = nums[l] <= target < nums[mid]
                if in_left:
                    r = mid - 1
                else:
                    l = mid + 1

            # RIGHT HALF SORTED
            else:

                in_right = nums[mid] < target <= nums[r]
                if in_right:
                    l = mid + 1
                else:
                    r = mid - 1

            step += 1
        return -1