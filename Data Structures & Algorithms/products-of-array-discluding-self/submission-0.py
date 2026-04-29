class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[0]*len(nums)
        prf=[1]*len(nums)
        suf=[1]*len(nums)

        for i in range(1,len(nums)):
            prf[i]=nums[i-1]*prf[i-1]

        for j in range(len(nums)-2,-1,-1):
            suf[j]=nums[j+1]*suf[j+1]

        for i in range(len(nums)):
            res[i]=prf[i]*suf[i]  

        return res      
        