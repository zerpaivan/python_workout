# script para covertir una frase en ingles a pig latin.
# utilizando el ejercicio anterior:git

from pig_latin import PigLatin
my_sentence = "my cat is called pepito"

def pl_sentence(sentence):
    words = sentence.split(" ")
    print(words)
    pig_words = []
    for word in words:
        pig_word = PigLatin(word)
        pig_words.append(pig_word.word_to_pl())
    
    return " ".join(pig_words)


if __name__ == "__main__":
    print(pl_sentence(my_sentence))
