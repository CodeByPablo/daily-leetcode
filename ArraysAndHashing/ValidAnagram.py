from typing import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Initial personal solution
        # if len(s) == len(t):
        #     chars = list(s)
        #     for i in range(len(t)):
        #         if t[i] not in chars:
        #             return False
        #         chars.remove(t[i])
        #     return True
        # return False

        # HashMap solution 1
        # if len(s) == len(t):
        #     chars = {}
        #     length = len(s)
        #     for i in range(length):
        #         if s[i] not in chars:
        #             chars[s[i]] = 1
        #         else:
        #             chars[s[i]] += 1
        #     for i in range(length):
        #         if t[i] not in chars:
        #             return False
        #         elif chars[t[i]] > 0:
        #             chars[t[i]] -= 1
        #         else:
        #             return False
        #     return True
        # return False

        # HashMap solution 2 - Time: O(s+t) - Space: O(s+t)
        # if len(s) != len(t):
        #     return False
        
        # s_chars, t_chars = {}, {}
        # length = len(s)

        # for i in range(length):
        #     s_chars[s[i]] = 1 + s_chars.get(s[i], 0)
        #     t_chars[t[i]] = 1 + t_chars.get(t[i], 0)
        # for c in s_chars:
        #     if s_chars[c] != t_chars.get(c, 0):
        #         return False
        # return True

        # HashMap solution short
        return Counter(s) == Counter(t)

        # Sorting solution solution
        # return sorted(s) == sorted(t)



solution = Solution()
print(solution.isAnagram("asscasaacc", "casacaassc"))