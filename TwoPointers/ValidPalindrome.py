
class Solution:
    def isPalindrome(self, s:str) -> bool:
        # isalpha function using extra memory
        # new_str = ""

        # for c in s:
        #     if c.isalpha():
        #         new_str += c.lower()
        
        # return new_str == new_str[::-1]

        # ascii verification
        p1, p2 = 0, len(s) - 1

        while p1 < p2:
            while p1 < p2 and not self.isAlphanum(s[p1]):
                p1 += 1
            while p2 > p1 and not self.isAlphanum(s[p2]):
                p2 -= 1
                
            if s[p1].lower() != s[p2].lower():
                return False
            p1 += 1
            p2 -= 1
        
        return True
    
    def isAlphanum(self, c) -> bool:
        return ((ord('A') <= ord(c) <= ord('Z')) or
                (ord('a') <= ord(c) <= ord('z')) or
                (ord('0') <= ord(c) <= ord('9')))

solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal: Panama"))
