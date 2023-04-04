
PLACEHOLDER = "[names]"

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as file:
    data = file.read()
    for name in names:
        stripped_name = name.strip()
        data = data.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="a+") as written_file:
            written_file.write(data)
