import pandas

phonetic_data = pandas.read_csv("NATO-alphabet-start\\nato_phonetic_alphabet.csv", index_col='letter')

phonetic_alphabet = pandas.DataFrame.to_dict(phonetic_data)

print(phonetic_alphabet['code']['A'])
student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass


student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = "hi"

list_of_letters = [letter for letter in user_input.upper()]
print(list_of_letters)

phonetic_dict = {key:value for (key, value) in phonetic_alphabet['code'].items() if key in list_of_letters}
print(phonetic_dict)

# phonetic_dict = {phonetic_letter:letter for (phonetic_letter, letter) in phonetic_alphabet.values() if phonetic_data['code'].keys == letter in list_of_letters}
# print(phonetic_dict)
