from collections import deque
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 0:
            return 0
        l = 0
        res = 0
        freq = {}
        max_freq = None
        for r, ch in enumerate(s):
            freq[ch] = freq.get(ch, 0) + 1
            max_freq = max(freq, key=freq.get)
            while (r - l + 1) - freq[max_freq] > k:
                freq[s[l]] = freq.get(s[l], 0) - 1
                l += 1
                max_freq = max(freq, key=freq.get)
                #if freq.get(s[l]) == 0:
                    #freq.pop(s[l])
            res = max(res, r-l+1)
        return res