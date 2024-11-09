#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Mail Merge Project Start\\Input\\Letters\\starting_letter.txt", mode="r") as starting_letter:
    starting_letter_string = starting_letter.read()

with open("Mail Merge Project Start\\Input\\Names\\invited_names.txt", "r") as list_of_names:
    for name in list_of_names.readlines():
        letter_corrected = starting_letter_string.replace("[name]", name.strip())
        with open(f"Mail Merge Project Start\\Output\\ReadyToSend\\{name.strip()}_invite.txt", mode="w") as new_letter:
            new_letter.write(letter_corrected)

#print(starting_letter_string)


#print(list_of_names.readlines())