class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arrayMap = {}

        for i, n in enumerate (nums):
            diff = target - n
            if diff in arrayMap:
                return[arrayMap[diff], i]
            arrayMap[n] = i
        return 