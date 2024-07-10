from typing import List

class Solution:
    
    def encode(self, strs: List[str]) -> str:
        encode_msg = ""
        for i, w in enumerate(strs):
            encode_msg = encode_msg + w
            if i < len(strs) - 1:
                encode_msg += ":;"
        return self.decode(encode_msg)
    
    def decode(self, strs: str) -> List[str]:
        return strs.split(":;")

solution = Solution()
print(solution.encode(["Bibi","es","puta"]))
