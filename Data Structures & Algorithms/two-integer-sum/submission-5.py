class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        myMap = {}

        for i in range(len(nums)):
            if nums[i] in myMap:
                return [myMap[nums[i]], i]
            complement = target - nums[i]
            myMap[complement] = i