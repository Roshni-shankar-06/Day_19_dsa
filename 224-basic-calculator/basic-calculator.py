class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        current_result = 0
        current_number = 0
        sign = 1  # 1 represents '+', -1 represents '-'
        
        for char in s:
            if char.isdigit():
                # Build the multi-digit number
                current_number = current_number * 10 + int(char)
                
            elif char == '+':
                # Evaluate the expression to the left
                current_result += sign * current_number
                # Update sign and reset the current number
              
