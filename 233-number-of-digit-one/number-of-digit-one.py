class Solution:
    def countDigitOne(self, n: int) -> int:
        ans = 0
        pow10 = 1
        while pow10 <= n:
            divisor = pow10 * 10
            quotient = n // divisor
            remainder = n % divisor
            
            if quotient > 0:
             
