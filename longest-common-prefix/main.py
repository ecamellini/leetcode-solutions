from typing import List


class Solution:
    def longestCommonPrefixA(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        longestPrefix = min(strs, key=len)

        for word in strs:
            for i, char in enumerate(longestPrefix):
                if char == word[i]:
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
            for word in strs:
                if not word.startswith(longestPrefix):
                    isItReallyACommonPrefix = False
                    break

            if isItReallyACommonPrefix:
                return longestPrefix
            else:
                longestPrefix = longestPrefix[:-1]

        return ""


sol = Solution()

assert sol.longestCommonPrefixA([]) == ""
assert sol.longestCommonPrefixB(["hello"]) == "hello"
assert sol.longestCommonPrefixA(["flower", "flow", "flight"]) == "fl"
assert sol.longestCommonPrefixB(["dog", "racecar", "car"]) == ""
assert sol.longestCommonPrefixA(["dog", "doggy", "doggone"]) == "dog"
assert sol.longestCommonPrefixB(["ab", "a"]) == "a"
print("All tests have passed.")
