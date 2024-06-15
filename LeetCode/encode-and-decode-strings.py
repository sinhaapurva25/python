from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return
        if len(strs) == 1:
            if strs[0] == "":
                return strs[0]
        return ":;".join(strs)

    def decode(self, s: str) -> List[str]:
        if s is None:
            return []
        if s == "":
            return [""]
        return s.split(":;")