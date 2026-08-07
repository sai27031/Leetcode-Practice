class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        for i in range(1,len(nums)):
            left[i] = left[i-1] * nums[i-1]
        right = [1] * len(nums)
        for i in range(len(nums)-2, -1, -1):
            right[i] = right[i+1] * nums[i+1]
        answer = [1] * len(nums)
        for i in range(len(nums)):
            answer[i] = left[i] * right[i]
        return answer