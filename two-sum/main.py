from typing import List


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, numA in enumerate(nums):
            for j, numB in enumerate(nums[i+1:], start=i+1):
                if numA + numB == target:
                    return [i, j]


if __name__ == "__main__":
    assert Solution().twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert Solution().twoSum([3, 7, 11, 15, 3, 7, 11], 18) == [0, 3]
    assert Solution().twoSum([3, 2, 4], 6) == [1, 2]
    assert Solution().twoSum([3, 3], 6) == [0, 1]
