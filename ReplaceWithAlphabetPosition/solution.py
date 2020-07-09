import string

def alphabet_position(text):
    alphabet = {char: i for i,char in enumerate(string.ascii_lowercase)}
    text2 = text.lower()
    text3 = [i for i in text2 if i.isalpha() == True ]
    lst = []
    for i in text3:
        for k, v in alphabet.items():
            if i == k:
                lst.append(v + 1)
    print(' '.join(str(e) for e in lst))
    return ' '.join(str(e) for e in lst)

alphabet_position("The sunset sets at twelve o' clock.")