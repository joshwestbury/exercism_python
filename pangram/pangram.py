def is_pangram(sent):
    letters = "abcdefghijklmnopqrstuvwxyz"
    letters = list(letters)
    sent = sent.lower()
    sent = sent.replace(" ", "")

    lst = []
    for i in sent:
        if i in letters:
            lst.append(i)

    lst = set(lst)

    if len(lst) == len(letters):
        return True
    else:
        return False


is_pangram("The quick brown fox jumps over the lazy dog")
