class Solution {
    public String fractionToDecimal(int numerator, int denominator) {
        if (numerator == 0) {
            return "0";
        }
        
        StringBuilder result = new StringBuilder();
        
        // Handle signs for negative numbers
        if ((numerator < 0) ^ (denominator < 0)) {
            result.append("-");
        }
        
        // Convert to long to prevent overflow (e.g., Integer.MIN_VALUE)
        long num = Math.abs((long) numerator);
        long den = Math.abs((long) denominator);
        
        // Append integer part
        result.append(num / den);
        long remainder = num % den;
        
        if (remainder == 0) {
            return result.toString();
        }
        
        // Append decimal point
        result.append(".");
        
    
        
