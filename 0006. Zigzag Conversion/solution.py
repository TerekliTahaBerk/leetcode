class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        index, step = 0, 1  # index: hangi satırdayız, step: yön belirleme
        
        for char in s:
            rows[index] += char
            if index == 0:
                step = 1  # Aşağı doğru git
            elif index == numRows - 1:
                step = -1  # Yukarı doğru git
            index += step  # Bir sonraki satıra geç
        
        return "".join(rows)
