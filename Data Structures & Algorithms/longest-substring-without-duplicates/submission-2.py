class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1
        se = list(s)
        seen = {se[0]: 1}
        list2 = [se[0]]
        l = 0
        r = 0
        res = 1
        while r < len(s)-1:
            r+=1
            seen[se[r]] = seen.get(se[r], 0) + 1
            list2.append(se[r])
            while seen[se[r]] > 1:
                seen[se[l]] = seen.get(se[l], 0) - 1
                list2.remove(se[l])
                l += 1
            if len(list2) > res:
                res = len(list2)
        return res