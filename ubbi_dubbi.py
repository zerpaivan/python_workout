# script para convertir unapalabra en ingles a 
# "Ubbi Dubbi" (idioma de juego de niños estadounidenses)
# regla: cada vocal es precedida por ub ejm: dog -dubog, python - pythubon

class Ubbi_dubbi():
    def __init__(self, word: str):
        self.word = word
    
    def world_to_ubbidubbi(self):
        vowels = "aeiou"
        ud_word = ""
        for letter in self.word:
            if letter in vowels:
                ud_word = ud_word + "ub" + letter
            else:
                ud_word = ud_word + letter
        
        return ud_word

if __name__ == "__main__":
    my_word = Ubbi_dubbi("phone")
    print(my_word.world_to_ubbidubbi())



