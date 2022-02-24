class Solution:
    def addDigits(self, num: int) -> int:
        numStr = str(num)

        digitsSum = 0

        for digit in numStr:
            digitsSum += int(digit)

        if len(str(digitsSum)) == 1:
            return digitsSum
        else:
            return self.addDigits(digitsSum)


sol = Solution()
assert sol.addDigits(38) == 2
print("All tests have passed")
