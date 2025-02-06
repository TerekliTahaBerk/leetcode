class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # 32-bit sınırlarını tanımlayalım
        INT_MAX = 2**31 - 1  # 2147483647
        INT_MIN = -2**31     # -2147483648
        
        # İşareti belirle (negatif olup olmadığını kontrol et)
        negative = (dividend < 0) ^ (divisor < 0)
        
        # Mutlak değerleri al
        dividend, divisor = abs(dividend), abs(divisor)
        
        quotient = 0  # Bölme sonucu
        
        while dividend >= divisor:
            temp, multiple = divisor, 1
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            
            dividend -= temp
            quotient += multiple
        
        # İşareti uygula
        quotient = -quotient if negative else quotient
        
        # 32-bit sınırlarını uygula
        return max(min(quotient, INT_MAX), INT_MIN)
