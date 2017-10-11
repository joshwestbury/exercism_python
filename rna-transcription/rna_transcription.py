seq = input("What is the dna sequence? ").upper()


def rightLetters(x):
    letter = ["G", "C", "T", "A"]

    if (x in letter):
        return True
    else:
        return False


seq = filter(rightLetters, seq)

seq = (list(seq))


def to_rna(seq):
    #seq = seq.upper()
    #seq = list(seq)

    ans = []
    for i in seq:
        if i == "G":
            ans.append("C")
        elif i == "C":
            ans.append("G")
        elif i == "T":
            ans.append("A")
        elif i == "A":
            ans.append("U")
        else:
            pass

    ans = "".join(ans)
    # print(ans)
    return ans


to_rna(seq)
