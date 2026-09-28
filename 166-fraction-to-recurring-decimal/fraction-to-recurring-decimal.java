class Solution {
    public String fractionToDecimal(int numerator, int denominator) {
        if (numerator == 0) {
            return "0";
        }
        
        StringBuilder result = new StringBuilder();
        
        // Handle signs for negative numbers
        if ((numerator < 0) ^ (denominator < 0)) {
            result.append("-");
      
