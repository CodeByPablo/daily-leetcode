from typing import List

class Solution:
    
    def encode(self, strs: List[str]) -> str:
        encode_msg = ""
        for w in strs:
            encode_msg = encode_msg + w + " "
        return self.decode(encode_msg)
    
    def decode(self, strs: str) -> List[str]:
        return strs.split(" ")

solution = Solution()
print(solution.encode(["Bibi","es","puta"]))
