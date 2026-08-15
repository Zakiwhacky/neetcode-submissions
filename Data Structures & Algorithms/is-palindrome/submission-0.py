class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        s = s.lower()
        clean = re.sub(r'[^A-Za-z0-9]', '', s)
        arr = []

        for i in clean:
            arr.append(ord(i))
        print(arr, list(reversed(arr)))
        if arr == list(reversed(arr)):
            return True
        else:
            return False


