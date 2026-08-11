class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myMap={}
        out=[]
        outout=[]
        for i in nums:
            if i not in myMap:
                myMap[i]=1
            else:
                myMap[i]+=1
        myMap = dict(sorted(myMap.items(), key = lambda item: item[1], reverse=True))
        for key in myMap:
            out.append(key)
        for x in range (k):
            outout.append(out[x])
        return outout
            