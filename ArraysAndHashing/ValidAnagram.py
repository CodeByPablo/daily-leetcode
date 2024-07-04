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

        # HashMap solution 2
        if len(s) == len(t):
            s_chars = {}
            t_chars = {}
            length = len(s)

            for i in range(length):
                if s[i] not in s_chars:
                    s_chars[s[i]] = 1
                else:
                    s_chars[s[i]] += 1
            for i in range(length):
                if t[i] not in t_chars:
                    t_chars[t[i]] = 1
                else:
                    t_chars[t[i]] += 1
            
            if s_chars == t_chars:
                return True
        return False



solution = Solution()
print(solution.isAnagram("asscasaacc", "casacaassc"))