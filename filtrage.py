def filter(mot):
    if len(mot) > 3:
        if mot.endswith("ies"):
            mot = mot[:-3]
        elif mot.endswith("s"):
            mot = mot[:-1]
        elif mot.endswith("ed") and voyelle(mot[:-2]):
            mot = mot[:-2]
        elif mot.endswith("y"):
            mot = mot[:-1] + "i"
        elif len(mot) > 6:
            if mot.endswith("ation") and m(mot) > 2:
                mot = mot[:-5] + "ate"
        elif mot.endswith("ant") and m(mot) > 1:
            mot = mot[:-3]
        elif mot.endswith("ss") and m(mot) > 1:
            mot = mot[:-2]
        elif mot.endswith("al") and m(mot) > 1:
            mot = mot[:-2]
        elif mot.endswith("e") and m(mot) > 1:
            mot = mot[:-1]
        elif mot.endswith("t") and m(mot[:-1]):
            mot = mot[:-1]
    return mot

def voyelle(mot):
    vowels = "aeiou"
    return any(char in vowels for char in mot)

def m(mot):
    vowels = "aeiou"
    count = 0
    in_vowel = False
    for char in mot:
        if char in vowels:
            if not in_vowel:
                count += 1
            in_vowel = True
        else:
            in_vowel = False
    return count
