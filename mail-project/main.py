#TODO: Create a letter using starting_letter.txt

import os
INPUT_FILE_PATH = "/home/oziel/Documents/mail-project/Input/Letters/starting_letter.txt"
OUTPUT_DIR = "/home/oziel/Documents/mail-project/Output/ReadyToSend"
PLACEHOLDER = "[name]"

with (open("Input/Names/invited_names.txt") as invited_names):
    for names in invited_names:
        name = names.strip()
        output_file_path = os.path.join(OUTPUT_DIR, f"letter_for_{name}")
        with (
            open(INPUT_FILE_PATH, mode="r") as starting_letter,
            open(output_file_path, mode="w") as outfile
        ):
            for letter in starting_letter:
                new_letter = letter.replace(PLACEHOLDER, name)
                outfile.write(new_letter)

