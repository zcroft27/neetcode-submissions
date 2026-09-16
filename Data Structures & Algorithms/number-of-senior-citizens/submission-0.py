class Solution:
    def countSeniors(self, details: List[str]) -> int:
        def get_age(id_string: str) -> int:
            return int(id_string[11:13])
        
        return len(list(filter(lambda curr: curr > 60, map(get_age, details))))