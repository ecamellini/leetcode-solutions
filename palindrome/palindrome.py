class Solution:
    def isPalindrome(self, num: int) -> bool:
        numStr = str(num)

        for i, digit in enumerate(numStr):
            if digit != numStr[-(i+1)]:
                return False

        return True


if __name__ == "__main__":
    sol = Solution()
    assert sol.isPalindrome(121) is True
    assert sol.isPalindrome(1221) is True
    assert sol.isPalindrome(1222) is False
    assert sol.isPalindrome(213123213213) is False
    assert sol.isPalindrome(123456890098654321) is True
