class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Initial personal solution
        if len(s) == len(t):
            chars = list(s)
            for i in range(len(t)):
                if t[i] not in chars:
                    return False
                chars.remove(t[i])
            return True
        return False

solution = Solution()
print(solution.isAnagram("anagram", "nagaram"))