class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.replace(" ","")
        s=s.lower()
        for i in s:
            if not i.isalnum():
                s=s.replace(i,"")
        srev=s[::-1]
        return s==srev