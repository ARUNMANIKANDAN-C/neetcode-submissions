class Solution:
    def climbStairs(self, n):
        if n <= 2:
            return n

        def multiply(A, B):
            return [
                [
                    A[0][0] * B[0][0] + A[0][1] * B[1][0],
                    A[0][0] * B[0][1] + A[0][1] * B[1][1]
                ],
                [
                    A[1][0] * B[0][0] + A[1][1] * B[1][0],
                    A[1][0] * B[0][1] + A[1][1] * B[1][1]
                ]
            ]

        def power(matrix, p):
            result = [[1, 0], [0, 1]]  # Identity matrix

            while p > 0:
                if p % 2 == 1:
                    result = multiply(result, matrix)

                matrix = multiply(matrix, matrix)
                p //= 2

            return result

        base = [[1, 1],
                [1, 0]]

        res = power(base, n+1)

        return res[0][1]