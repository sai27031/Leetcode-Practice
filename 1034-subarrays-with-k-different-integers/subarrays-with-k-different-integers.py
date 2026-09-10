class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        result = 0
        left_far=0
        left_near=0
        for right in range(len(nums)):
            count[nums[right]] += 1
            while len(count) > k:
                count[nums[left_near]] -= 1
                if count[nums[left_near]] == 0:
                    count.pop(nums[left_near])
                left_near += 1
                left_far = left_near
            while count[nums[left_near]] > 1:
                count[nums[left_near]] -= 1
                left_near += 1
            if len(count) == k:
                result += left_near - left_far + 1
        return result 
