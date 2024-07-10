from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # initial solution - Time: O(n + m^2)
        # seen = {}
        # top_frequent = []

        # for i in range(len(nums)):
        #     if nums[i] in seen:
        #         seen[nums[i]] += 1
        #     else:
        #         seen[nums[i]] = 1

        # for n in range(k):
        #     max_key = max(seen, key=seen.get)
        #     top_frequent.append(max_key)
        #     seen.pop(max_key)
        # return top_frequent

        # bucket sort - Time: O(n)
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for num, count in count.items():
            freq[count].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

solution = Solution()
print(solution.topKFrequent([1,1,1,2,2,3,4,4,4,4,4], 2))