class Solution:
    def reverse(self, x: int) -> int:
        # İşaret bilgisini al
        sign = -1 if x < 0 else 1

        # Sayının mutlak değerini tersine çevir
        reversed_x = int(str(abs(x))[::-1])

        # 32-bit integer aralığını kontrol et
        if reversed_x > 2**31 - 1:
            return 0

        return sign * reversed_x
