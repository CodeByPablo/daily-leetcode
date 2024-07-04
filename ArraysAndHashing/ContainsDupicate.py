from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Brute force solution - Time: O(n^2) - Space: O(1)
        # for i in range(len(nums) - 1):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False

        # Sorting solution - Time: O(nlogn) - Space: O(1)
        # Sort the array
        # n = len(nums)
        # for i in range(n):
        #     for j in range(0, n - i - 1):
        #         if nums[j] > nums[j + 1]:
        #             nums[j], nums[j + 1] = nums[j + 1], nums[j]
        # print(nums)
        # # Compare 2 adyacent numbers
        # for i in range(n - 1):
        #     if nums[i] == nums[i + 1]:
        #         return True
        # return False

        # HashSet solution - Time: O(n) - Space: O(n)
        seen = set()
        for i in range(len(nums)):
            if nums[i] in seen:
                    return True
            seen.add(nums[i])
        return False


solution = Solution()
print(solution.containsDuplicate([1,3,5,2,4,5,6,3,3,4,7]))