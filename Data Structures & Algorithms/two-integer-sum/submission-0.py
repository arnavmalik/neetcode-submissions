class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myMap = {}
        for i in range(0,len(nums)):
            x = target - nums[i]
            if x in myMap and myMap[x]<i:
                return [myMap[x],i]
            elif x in myMap and myMap[x]>i:
                return [i,myMap[x]]
            myMap[nums[i]]=i