from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # My initial solution - Time: O(n) - Space: O(n)
        left = [1] * len(nums)
        right = [1] * len(nums)

        for i in range(len(nums) - 1):
            left[i + 1] = left[i] * nums[i]
        for i in range(len(nums) - 1, 0, -1):
            right[i - 1] = right[i] * nums[i]
        return [left[i] * right[i] for i in range(len(left))]


solution = Solution()
print(solution.productExceptSelf([4,7,2,9,2]))



nums = [4,7,2,9,2]
print(range(len(nums) - 1, 0, -1))