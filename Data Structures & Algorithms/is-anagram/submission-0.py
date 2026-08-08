class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t)!=len(s):
            return False
        counter = {}
        for i in s:
            if i in counter:
                counter[i] = counter[i] + 1
            else:
                counter[i] = 1
        for j in t:
            if j in counter:
                counter[j] = counter[j] - 1
        for val in counter.values():
            if val!=0:
                return False
        return True
