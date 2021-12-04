import pandas


df = pandas.read_csv("nato_phonetic_alphabet.csv")

code_dict = {row.letter:row.code for (index, row) in df.iterrows()}
print(code_dict)

word = input("Enter word.").upper()
output = [code_dict[letter] for letter in word]

print(output)
