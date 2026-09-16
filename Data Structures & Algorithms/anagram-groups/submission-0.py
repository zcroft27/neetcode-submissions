class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        frequencies_to_list = defaultdict(list)
        for st in strs:
            arr = [0] * 26
            self.getFrequency(arr, st)
            frequencies_to_list[tuple(arr)].append(st)
        return list(frequencies_to_list.values())

        return resp

    def getFrequency(self, arr, st):
        for char in st:
            arr[ord(char) - ord('a')] += 1