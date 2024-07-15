
class Solution:
    def isPalindrome(self, s:str) -> bool:
        # isalpha function using extra memory
        new_str = ""

        for c in s:
            if c.isalpha():
                new_str += c.lower()
        
        return new_str == new_str[::-1]

solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal: Panama"))
