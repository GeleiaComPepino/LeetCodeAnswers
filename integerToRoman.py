class Solution:
    def intToRoman(self, num: int) -> str:
        valores = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        simbolos = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
        
        resultado = ""
        for i in range(len(valores)):
            while num >= valores[i]:
                num -= valores[i]
                resultado += simbolos[i]
        return resultado

