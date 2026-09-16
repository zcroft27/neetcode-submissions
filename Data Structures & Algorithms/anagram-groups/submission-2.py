class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_to_list = defaultdict(list)
        for word in strs:
            seen = [0]*26
            for char in word:
                seen[ord(char)-ord('a')] += 1
            freq_to_list[tuple(seen)].append(word)
        
        ret = []
        for lst in freq_to_list.values():
            ret.append(lst)
        
        return ret