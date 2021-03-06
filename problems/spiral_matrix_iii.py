from typing import List


class Solution:
    def spiralMatrixIII_deprecated(
        self, R: int, C: int, r0: int, c0: int
    ) -> List[List[int]]:
        # Runtime: 116 ms, faster than 84.62% of Python3 online submissions for
        # Spiral Matrix III. Memory Usage: 14.9 MB, less than 48.61% of Python3
        # online submissions for Spiral Matrix III.
        i, j = r0, c0
        # right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        count, stride = 0, 1
        result = [[i, j]]
        while len(result) < R * C:
            dx, dy = directions[count]

            for step in range(stride):
                i, j = i + dx, j + dy
                if 0 <= i < R and 0 <= j < C:
                    result.append([i, j])

            # increase stride whenever we have used same stride 2 times.
            count += 1
            if count % 2 == 0:
                stride += 1
            if count % 4 == 0:
                count = 0

        return result

    def spiralMatrixIII(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        # Loop unrolling - 2 loops in 1 loop. Runtime: 112 ms, faster than 92.60% of
        # Python3 online submissions for Spiral Matrix III. Memory Usage: 14.9 MB,
        # less than 17.59% of Python3 online submissions for Spiral Matrix III.
        i, j = r0, c0
        sign, stride = 1, 1
        result = [[i, j]]
        while len(result) < R * C:
            for step in range(stride):
                j += sign
                if 0 <= i < R and 0 <= j < C:
                    result.append([i, j])

            for step in range(stride):
                i += sign
                if 0 <= i < R and 0 <= j < C:
                    result.append([i, j])

            stride += 1
            sign *= -1

        return result
