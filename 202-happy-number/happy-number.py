class Solution:
    def isHappy(self, n: int) -> bool:
        def square(num: int) -> int:
            ans = 0
            while num > 0:
                remainder = num % 10
                ans += remainder * remainder
                num //= 10
            return ans

        slow = n
        fast = n

        while True:
            slow = square(slow)
            fast = square(square(fast))
            if slow == fast:
                break
        
        return slow == 1