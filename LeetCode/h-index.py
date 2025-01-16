from typing import List
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        for i in range(len(citations)):
            v = citations[i]
            if len(citations) - i <= v:
                return len(citations) - i
        return 0
s = Solution()
s.hIndex(citations = [3,0,6,1,5])
