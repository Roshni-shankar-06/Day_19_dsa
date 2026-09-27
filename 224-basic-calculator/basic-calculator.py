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
                sign = 1
                current_number = 0
                
            elif char == '-':
                # Evaluate the expression to the left
                current_result += sign * current_number
                # Update sign and reset the current number
                sign = -1
                current_number = 0
                
            elif char == '(':
                # Push the current result and sign to the stack
                stack.append(current_result)
                stack.append(sign)
                # Reset result and sign for the new sub-expression
                current_result = 0
                sign = 1
                
            elif char == ')':
                # Evaluate the last number before the closing parenthesis
                current_result += sign * current_number
                current_number = 0
                
                # Pop the sign and the previous result from the stack
                saved_sign = stack.pop()
                saved_result = stack.pop()
                
                # Apply the sign to the parenthesis result and add it to the outer result
                current_result = saved_result + (saved_sign * current_result)
        
        # Add any remaining number at the end of the string
        return current_result + (sign * current_number)
