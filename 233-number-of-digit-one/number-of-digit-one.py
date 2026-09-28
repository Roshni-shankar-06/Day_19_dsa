class Solution:
    def countDigitOne(self, n: int) -> int:
        ans = 0
        pow10 = 1
        while pow10 <= n:
            divisor = pow10 * 10
           
