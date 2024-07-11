from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # My initial solution - Time: O(n) - Space: O(n)
        # left = [1] * len(nums)
        # right = [1] * len(nums)

        # for i in range(len(nums) - 1):
        #     left[i + 1] = left[i] * nums[i]
        # for i in range(len(nums) - 1, 0, -1):
        #     right[i - 1] = right[i] * nums[i]
        # return [left[i] * right[i] for i in range(len(left))]

        # Improvement - Space: O(1)
        res = [1] * len(nums)
        
        left_product = 1
        for i in range(len(nums)):
            res[i] = left_product
            left_product *= nums[i]

        right_product = 1
        for i in range(len(nums) - 1, -1, -1): #range(start, stop (not included), step)
            res[i] *= right_product
            right_product *= nums[i]
        
        return res

solution = Solution()
print(solution.productExceptSelf([4,7,2,9,2]))