words = ['racecar', 'noon', 'civic']


def reverse_word(word):
    reserved = ""
    for letter in word:
        reserved = letter + reserved
    return reserved


def is_palindrome(word):
    return word == reverse_word(word)


def check_all_palindromes(arr):
    for word in arr:
        if not is_palindrome(word):
            return print("False")
    return print("True")


def create_staircase(nums):
    step = 1
    subsets = []
    while len(nums) != 0:
        if len(nums) >= step:
            subsets.append(nums[0:step])
            nums = nums[step:]
            step += 1
        else:
            return print("False")
    return print(subsets)


list_n = [1, 2, 3, 4, 5, 6]

create_staircase(list_n)

