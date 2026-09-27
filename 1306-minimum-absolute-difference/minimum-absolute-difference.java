import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public List<List<Integer>> minimumAbsDifference(int[] arr) {
        List<List<Integer>> result = new ArrayList<>();
        
        // Step 1: Sort the array
        Arrays.sort(arr);
        
        int minDiff = Integer.MAX_VALUE;
        
        // Step 2: Single pass to find minimum difference and build the result
        for (int i = 0; i < arr.length - 1; i++) {
            int currentDiff = arr[i + 1] - arr[i];
            
            if (currentDiff < minDiff) {
                // Found a smaller difference: update minDiff and reset the list
                minDiff = currentDiff;
                result.clear();
                result.add(Arrays.asList(arr[i], arr[i + 1]));
            } else if (currentDiff == minDiff) {
                // Found another pair with the same minimum difference: add to list
                result.add(Arrays.asList(arr[i], arr[i + 1]));
            }
        }
        
        return result;
    }
}
