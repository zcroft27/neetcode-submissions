class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        frequencies_to_list = defaultdict(list)

        for string in strs:
            arr = [0] * 26
            for char in string:
                arr[ord(char) - ord('a')] += 1
            frequencies_to_list[tuple(arr)].append(string)
        
        return list(frequencies_to_list.values())