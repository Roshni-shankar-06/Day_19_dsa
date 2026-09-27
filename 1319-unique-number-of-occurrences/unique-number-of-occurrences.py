from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        # Step 1: Count the occurrences of each number
        counts = Counter(arr)
        
        # Step 2: Compare the number of unique counts to the total number of unique elements
        return len(counts) == len(set(counts.values()))
