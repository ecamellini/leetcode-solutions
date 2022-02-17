from typing import List


class Solution:
    def longestCommonPrefixA(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        longestPrefix = min(strs, key=len)
        for str in strs:
            # maxLengthOfCommonPrefix = min(len(longestPrefix), len(str))
            for i in range(len(longestPrefix)):
                if longestPrefix[i] == str[i]:
                    continue
                else:
                    longestPrefix = longestPrefix[0:i]
                    break

        return longestPrefix

    def longestCommonPrefixB(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        longestPrefix = min(strs, key=len)
        while len(longestPrefix) > 0:

            isItReallyACommonPrefix = True
            for s in strs:
                if not s.startswith(longestPrefix):
                    isItReallyACommonPrefix = False
                    break

            if isItReallyACommonPrefix:
                return longestPrefix
            else:
                longestPrefix = longestPrefix[:-1]

        # No prefix
        return ""


sol = Solution()

assert sol.longestCommonPrefixA([]) == ""
assert sol.longestCommonPrefixB(["hello"]) == "hello"
assert sol.longestCommonPrefixA(["flower", "flow", "flight"]) == "fl"
assert sol.longestCommonPrefixB(["dog", "racecar", "car"]) == ""
assert sol.longestCommonPrefixA(["dog", "doggy", "doggone"]) == "dog"
assert sol.longestCommonPrefixB(["ab", "a"]) == "a"
print("All tests have passed.")
