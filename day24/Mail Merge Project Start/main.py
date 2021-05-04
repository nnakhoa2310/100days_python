PLACE_HOLDER = "[name]"
with open("Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
with open("Input/Letters/starting_letter.txt") as letters_file:
    letters_content = letters_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letters = letters_content.replace(PLACE_HOLDER, stripped_name)
        with open(f"Output/ReadyToSend/letter_for_{stripped_name}.txt", mode= "w") as completed_letter:
            completed_letter.write(new_letters)