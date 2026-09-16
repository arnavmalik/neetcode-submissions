class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        hmap={"(":")", "{":"}", "[":"]"}
        for i in s:
            if i in hmap:
                stack.append(i)    
            elif i in hmap.values():
                key = next(k for k,v in hmap.items() if v == i)
                if not stack:
                    return False
                if stack[-1]==key:
                    stack.pop()
                else:
                    return False
            else:
                return False             
        if not stack:
            return True
        return False    