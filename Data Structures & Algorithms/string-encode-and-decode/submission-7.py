class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res += str(len(i)) + "#" + i
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            length_str = ""
            while i < len(s) and s[i] != "#":
                length_str += s[i]
                i += 1
            i += 1
            length = int(length_str)
            word = s[i : i + length]
            res.append(word)
            i+=length
        return res