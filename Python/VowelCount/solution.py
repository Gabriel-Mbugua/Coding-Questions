#my solution

def get_count(input_str):
    num_vowels = 0
    vowels = ['a', 'e', 'i', 'o', 'u']

    for i in input_str:
        for j in vowels:
            if i == j:
                num_vowels += 1    
    return num_vowels

#ideal solution

def getCount(s):
    return sum(c in 'aeiou' for c in s)

get_count("abracadabra")