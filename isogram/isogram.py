def is_isogram(string):
    string = string.lower()
    if string == "":
        return True

    validLetters = "abcdefghijklmnopqrstuvwxyz"
    newString = "".join([char for char in string if char in validLetters])

    lst = list(newString)
    newList = set(lst)

    if len(lst) == len(newList):
         return True
    else:
         return False

is_isogram("isogram")
