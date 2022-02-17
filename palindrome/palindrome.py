class Solution:
    def isPalindrome(self, x: int) -> bool:
        xStr = str(x)

        for i in range(0, len(xStr)):
            if xStr[i] != xStr[-(i+1)]:
                return False

        # Qua il ciclo è finito!
        return True


if __name__ == "__main__":
    sol = Solution()
    assert sol.isPalindrome(121) is True
    assert sol.isPalindrome(1221) is True
    assert sol.isPalindrome(1222) is False
    assert sol.isPalindrome(213123213213) is False
    assert sol.isPalindrome(123456890098654321) is True
