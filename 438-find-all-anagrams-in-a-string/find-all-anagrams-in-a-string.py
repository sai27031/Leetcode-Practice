class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        count1 = {}
        for char in p:
            count1[char] = count1.get(char , 0) + 1
        count2 = {}
        left = 0
        result = [ ]
        for right in range(len(s)):
            count2[s[right]] = count2.get(s[right], 0) + 1
            if right - left + 1 > len(p):
                count2[s[left]] -=1
                if count2[s[left]] == 0:
                    del count2[s[left]]
                left += 1
            if right - left + 1 == len(p):
                if count1 == count2:
                    result.append(left)
        return result