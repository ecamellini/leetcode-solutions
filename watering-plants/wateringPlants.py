from typing import List


class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        if plants == []:
            return 0

        currentPosition = -1
        steps = 0
        waterLeft = capacity

        while True:
            while waterLeft >= plants[currentPosition + 1]:
                currentPosition += 1
                steps += 1
                waterLeft = waterLeft - plants[currentPosition]

                if currentPosition == len(plants) - 1:
                    return steps

            steps += currentPosition + 1
            waterLeft = capacity
            steps += currentPosition + 1


solution = Solution()

assert solution.wateringPlants([2, 2, 3, 3], 5) == 14
assert solution.wateringPlants([1, 1, 1, 4, 2, 3], 4)
assert solution.wateringPlants([7, 7, 7, 7, 7, 7, 7], 8) == 49
assert solution.wateringPlants([], 6) == 0
print("All tests passed.")
