str1 = "Ala ma kota"
str2 = "Kot ma Ale"

def letters_in_both_strings(str1, str2):
    list_of_letters = []
    for letter in str1.lower():
        if str2.lower().count(letter) == 0 or list_of_letters.count(letter) != 0:
            pass
        else:
            list_of_letters.append(letter)
    return list_of_letters

print "Litery wystepujace w obu ciagach to: ", letters_in_both_strings(str1, str2)