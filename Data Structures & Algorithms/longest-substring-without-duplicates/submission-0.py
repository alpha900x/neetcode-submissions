class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sbstr = set()
        max = 0
        t = 0
        for i in range(len(s)):
            if s[i] not in sbstr:
                sbstr.add(s[i])
                if max < len(sbstr):
                    max = len(sbstr)
            else:
                if max < len(sbstr):
                    max = len(sbstr)
                while s[i] in sbstr:
                    sbstr.discard(s[t])
                    t+=1
                sbstr.add(s[i])
        return max