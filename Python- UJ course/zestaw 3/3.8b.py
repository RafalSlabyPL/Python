str1 = "Ala ma kota"
str2 = "Kot ma Ale dziala?"

def all_letters_in_both_strings_list(str1, str2):
    all_letters = []

    for letter in str1.lower():
        if all_letters.count(letter) == 0:
            all_letters.append(letter)
        else:
            continue

    for letter in str2.lower():
        if all_letters.count(letter) == 0:
            all_letters.append(letter)
        else:
            continue

    return all_letters


print all_letters_in_both_strings_list(str1, str2)

