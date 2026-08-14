class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ht={}
        for i in range(len(strs)):
            count = [0] * 26
            for j in strs[i]:
                count[ord(j)-ord("a")] += 1
            count = tuple(count)
            if count not in ht:
                ht[count] = [strs[i]]
            else:
                ht[count].append(strs[i])    
        return list(ht.values())