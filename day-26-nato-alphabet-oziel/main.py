import pandas

data = pandas.read_csv('nato_phonetic_alphabet.csv')
data_dict = {row.letter: row.code for (index, row) in data.iterrows()}


def nato_alphabet():
    word = input("Enter a word: ").upper()
    try:
        response = [data_dict[letter] for letter in word]
    except KeyError:
        print("Number typed was an Integer, please enter a text")
        nato_alphabet()
    else:
        print(response)


nato_alphabet()

# from tkinter import *
#
# # Creating a new window and configurations
# window = Tk()
# window.title("Widget Examples")
# window.minsize(width=500, height=500)
# window.config(padx=20, pady=20)
#
# # Labels
# label = Label(text="This is old text")
# label.config(text="This is new text")
# label.grid(row=0, column=0)
#
#
# # Buttons
# def action():
#     print("Do something")
#
#
# # calls action() when pressed
# button = Button(text="Click Me", command=action)
# button.grid(row=1, column=1)
#
# button2 = Button(text="New Button", command=action)
# button2.grid(row=0, column=3)
#
# # Entries
# entry = Entry(width=30)
# # Add some text to begin with
# entry.insert(END, string="Some text to begin with.")
# # Gets text in entry
# entry.grid(row=4, column=4)
#
# window.mainloop()
