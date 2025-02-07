class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        m, n = len(num1), len(num2)
        result = [0] * (m + n)

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                pos1, pos2 = i + j, i + j + 1

                total = mul + result[pos2]
                result[pos2] = total % 10
                result[pos1] += total // 10
        
        while result and result[0] == 0:
            result.pop(0)
        
        return ''.join(map(str, result))
