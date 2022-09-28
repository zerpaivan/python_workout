# script para convertir unapalabra en ingles a 
# "Ubbi Dubbi" (idioma de juego de niños estadounidenses)
# regla: cada vocal es precedida por ub ejm: dog -dubog, python - pythubon

class Ubbi_dubbi():
    def __init__(self, word: str):
        self.word = word
        self.cat = "misin"
    
    def world_to_ubbidubbi(self):
        vowels = "aeiou"
        ud_word = ""
        for letter in self.word:
            if letter in vowels:
                ud_word = ud_word + "ub" + letter
            else:
                ud_word = ud_word + letter
        
        return ud_word

# solucion por Regex
import re
def ubbiDubbi(input_word):
    ubbiRegex = re.compile(r'([aeiouAEIOU])')
    ubbidubbi_word = ubbiRegex.sub(r'ub\1', input_word)
    return ubbidubbi_word

if __name__ == "__main__":
    my_word = Ubbi_dubbi("phone")
    print(my_word.world_to_ubbidubbi())
    print("Regex: ", ubbiDubbi("Duck cat dog"))
    print(getattr(my_word,"cat"))



