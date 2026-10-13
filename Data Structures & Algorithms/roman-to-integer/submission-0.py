class Solution:
    def romanToInt(self, s: str) -> int:
        cur = 0
        end = len(s)
        i = 0
        res = 0
        while i < end:
            if i == end-1:
                if s[i] == "I":
                    curr = 1 
                elif s[i] == "V":
                    curr = 5
                elif s[i] == "X":
                    curr = 10
                elif s[i] == "L":
                    curr = 50
                elif s[i] == "C":
                    curr = 100
                elif s[i] == "D":
                    curr = 500
                elif s[i] == "M":
                    curr = 1000
                i+=1

            elif s[i] == "I": #I
                if s[i+1] == "V": #IV
                    curr = 4
                    i+=2
                elif s[i+1] == "X":#IX
                    curr = 9
                    i+=2
                else: #I
                    curr = 1
                    i+=1
            elif s[i] == "V":#V
                curr = 5
                i+=1
            elif s[i] == "X": #X
                if s[i+1] == "L":#XL
                    curr = 40
                    i+=2
                elif s[i+1] == "C": #XC
                    curr = 90
                    i+=2
                else:#X
                    curr = 10
                    i+=1
            elif s[i] == "L":#L
                curr = 50
                i+=1
            elif s[i] == "C":#C
                if s[i+1] == "D":#CD
                    curr = 400
                    i+=2
                elif s[i+1] == "M":#CM
                    curr = 900
                    i+=2
                else:#C
                    curr = 100
                    i+=1
            elif s[i] == "D":
                curr = 500
                i+=1
            else:
                curr = 1000
                i+=1
            res+=curr
        
        return res
