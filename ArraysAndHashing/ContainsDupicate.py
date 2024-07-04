from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums) - 1):
            j = i + 1
            for j in range(len(nums) - 1):
                if nums[i] == nums[j]:
                    return True
        return False

solution = Solution()
print(solution.containsDuplicate([1,3,5,2,1,5,6,3,1,4,7]))