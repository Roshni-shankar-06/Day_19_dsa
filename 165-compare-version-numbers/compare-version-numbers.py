class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        levels1 = version1.split('.')
        levels2 = version2.split('.')
        length = max(len(levels1), len(levels2))
        
        
         
