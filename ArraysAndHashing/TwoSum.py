from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_nums = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in seen_nums:
                return [seen_nums[comp], i]
            seen_nums[nums[i]] = i
        return []


solution = Solution()
print(solution.twoSum([11,2,6,5,96,23,41,23,6,8,9,11], 64))