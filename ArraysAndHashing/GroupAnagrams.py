from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            anagrams[tuple(count)].append(s)
        return list(anagrams.values())

        # Not using defaultdict
        # anagrams = {}
        # for s in strs:
        #     count = [0] * 26
        #     for c in s:
        #         count[ord(c) - ord('a')] += 1
        #     key = tuple(count)
        #     if key in anagrams:
        #         anagrams[key].append(s)
        #     else:
        #         anagrams[key] = [s]
        # return list(anagrams.values())

solution = Solution()
print(solution.groupAnagrams(["eat", "tae", "see", "ese", "asf"]))