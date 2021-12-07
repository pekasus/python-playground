import pandas
import pyttsx3

df = pandas.read_csv("nato_phonetic_alphabet.csv")

code_dict = {row.letter:row.code for (index, row) in df.iterrows()}
print(code_dict)

engine = pyttsx3.init()


def generate_phonetic():
    word = input("Enter word: ").upper()
    try:
        output = [code_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphavet, please.")
        generate_phonetic()
    else:
        print(output)
        for code in output:
            engine.say(code)
        engine.runAndWait()

# engine.save_to_file('Hello World', 'test.mp3')
# engine.runAndWait()

generate_phonetic()
