import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")
dic = {row.letter: row.code for (index, row) in df.iterrows()}
user_name = input("Type your name: ").upper()
final_list = [dic[letter] for letter in user_name]
print(final_list)
