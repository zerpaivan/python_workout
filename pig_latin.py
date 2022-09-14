# script para convertir una palabra, en ingles, a pig latin (leguaje secreto)
# reglas:
# 1.- si la palabra comienza con consonalte la primera letra se coloca al final de la
# palabra y se agrega al final "ay"
# 2.- si comienza en vocal se añade al final de la palabra way

class PigLatin():

    def __init__(self, word: str):
        self.word = word
    
    def word_to_pl(self):
        vowels = "aeiouAEIOU"
        if self.word[0] in vowels:
            return f"{self.word}way"
        else:
            return  f"{self.word[1:]}{self.word[0]}ay"

if __name__ == "__main__":
    word1 = PigLatin("cat")
    print(word1.word_to_pl())