class Solution:
    def romanToInt(self, s: str) -> int:
        #largest to smallest: add them up
        #smaller before larger: subtract smaller
        
        roman={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        res=0
        
        for i in range (len(s)):
            if i + 1 < len(s) and roman[s[i]] < roman[s[i+1]]:
                res -= roman[s[i]]
            else:
                res += roman[s[i]]
                
        return res
        
'''''
#another solution:
        dict={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        res=0
        prev=""
        for item in s:
            res+=dict.get(item)
            if(prev+item) in ["IV","IX","XL","XC","CD","CM"]:
                res-=2*dict.get(prev)
            prev=item
        return res
'''''