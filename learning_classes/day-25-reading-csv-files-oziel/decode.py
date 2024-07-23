import pandas as pd
message_file = "message_file.txt"


def is_triangular_number(num):
    return (8 * num + 1) ** 0.5 % 1 == 0


def reorder_file(input_file, output_file):
    df = pd.read_csv(input_file, sep=' ', header=None, names=['Number', 'Word'])
    df_reorder = df.sort_values(by='Number')
    df_reorder.to_csv(output_file, sep=' ', header=False, index=False)


def decode(input_file):
    reorder_file(input_file, 'reordered_message.txt')
    df = pd.read_csv('reordered_message.txt', sep=' ', header=None, names=['Number', 'Word'])
    decoded_word = []

    for index, row in df.iterrows():
        number = row['Number']
        word = row['Word']

        if is_triangular_number(number):
            decoded_word.append(word)

    decode_message = ' '.join(decoded_word)

    return print(decode_message)


decode(message_file)
