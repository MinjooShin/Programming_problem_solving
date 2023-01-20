class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str_lst = list(map(str, digits))
        num_str = "".join(str_lst)
        num = int(num_str) + 1
        result = list(str(num))
        result = list(map(int, result))

        return result