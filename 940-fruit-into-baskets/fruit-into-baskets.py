class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_len = 0
        left = 0
        right = 0
        my_dict = {}
        while right < len(fruits):
            my_dict[fruits[right]] = my_dict.get(fruits[right],0) + 1
            while len(my_dict) > 2:
                my_dict[fruits[left]] -= 1
                if my_dict[fruits[left]] == 0:
                    del my_dict[fruits[left]]
                left += 1
            if len(my_dict) <= 2:
                max_len = max(max_len , right - left + 1)
            right += 1
        return max_len

