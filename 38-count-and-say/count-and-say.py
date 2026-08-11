class Solution:
    def countAndSay(self, n: int) -> str:
        result = "1"
        for i in range(n - 1):
            current = []
            count = 1
            for i in range(1, len(result)):
                if result[i] == result[i - 1]:
                    count += 1
                else:
                    current.append(str(count))
                    current.append(result[i - 1])
                    count = 1
            current.append(str(count))
            current.append(result[-1])
            result = "".join(current)
        return result 