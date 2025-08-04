class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs2={}
        for i in strs:
            sorted_key=''.join(sorted(i))
            if sorted_key in strs2:
                strs2[sorted_key].append(i)
            else:
                strs2[sorted_key]=[i]
        return(list(strs2.values()))            

        
