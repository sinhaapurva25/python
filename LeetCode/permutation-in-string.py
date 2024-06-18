class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1_freq = self.getFreq(s1)

        if len(s2) < len(s1):
            return False
        for i in range(len(s2)-len(s1)+1):
            if self.getFreq(s2[i:i+len(s1)]) == s1_freq:
                return True
        return False

    def getFreq(self, s):
        frq = {}
        for i in range(len(s)):
            frq[s[i]] = 1 + frq.get(s[i], 0)
        return frq


s = Solution()
print(s.checkInclusion(s1 ="xqrpm", s2 ="xyzkabxmqpr") == True)
print(s.checkInclusion(s1 ="hello", s2 ="ooolleoooleh") == False)
print(s.checkInclusion(s1="adc", s2="dcda") == True)
print(s.checkInclusion(s1="ab", s2="eidbaooo") == True)
print(s.checkInclusion(s1="ab", s2="eidboaoo") == False)
print(s.checkInclusion(s1="ab", s2="ab") == True)
print(s.checkInclusion(s1="ab", s2="ba") == True)
print(s.checkInclusion(s1="ab", s2="a") == False)
print(s.checkInclusion(s1="ab", s2="aob0b") == False)
print(s.checkInclusion(s1="ab", s2="baaob0b") == True)

# Cloudflare Ray ID: 895213cc1ade9385 • Your IP: 2405:201:800e:41bc:f427:3eb0:29eb:91a9 • Performance & security by Cloudflare
