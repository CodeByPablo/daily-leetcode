from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # initial solution
        seen = {}
        top_frequent = []

        for i in range(len(nums)):
            if nums[i] in seen:
                seen[nums[i]] = 1 + seen.get(nums[i], 0)
            else:
                seen[nums[i]] = 1

        for n in range(k):
            max_key = max(seen, key=seen.get)
            top_frequent.append(max_key)
            seen.pop(max_key)
        return top_frequent

solution = Solution()
print(solution.topKFrequent([1,1,1,2,2,3,4,4,4,4,4], 3))