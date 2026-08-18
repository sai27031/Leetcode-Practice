class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        count = {}
        freq = {}
        for num in nums[:k]:
            count[num] = count.get(num,0) + 1
        for num in count:
            freq[num] = freq.get(num, 0) + 1
        for right in range(k,len(nums)):
            leaving = nums[right-k]
            count[leaving] -= 1
            if count[leaving] == 0:
                del count[leaving]
            entering = nums[right]
            count[entering] = count.get(entering , 0) + 1
            for num in count:
                freq[num] = freq.get(num ,0) + 1
        ans = -1
        for num in freq:
            if freq[num] == 1:
                ans = max(ans,num)
        return ans