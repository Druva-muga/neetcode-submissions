class Solution:
    def climbStairs(self, n: int) -> int:
        def fib(i):
            if i<=2:
                return i
            return fib(i-2)+fib(i-1)

        return fib(n)

        