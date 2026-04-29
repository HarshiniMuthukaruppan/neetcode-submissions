class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s=0
        sm=0

        for i in  range(1,len(nums)+1):
            sm^=i

        for i in nums:
            s^=i

        return s^sm
        