class Solution:
    def freq(self, s):
        dct = dict()
        for i in s:
            if i in dct:
                dct[i] += 1
            else:
                dct[i] = 1
        return dct
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNoteFreq = self.freq(ransomNote)
        magazineFreq = self.freq(magazine)
        res = True
        for key, val in ransomNoteFreq.items():
            if key not in magazineFreq.keys():
                res = False
            else:
                if val > magazineFreq[key]:
                    res = False
        return res
s = Solution()
print(s.canConstruct(ransomNote = "a", magazine = "b"))
print(s.canConstruct(ransomNote = "aa", magazine = "ab"))
print(s.canConstruct(ransomNote = "aa", magazine = "aab"))
print(s.canConstruct(ransomNote = "bg", magazine = "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj"))
# Next challenges:
# Stickers to Spell Word