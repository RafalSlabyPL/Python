# (z literami I, V, X, L, C, D, M)

def roman_to_number():
    x = 0
    roman_number = raw_input("Wpisz poprawna liczbe rzymska: ").upper()

    if roman_number.find("CM") != -1:
        x += 900
        roman_number = roman_number.replace("CM", "")

    x += roman_number.count("M") * 1000

    x += roman_number.count("D") * 500

    if roman_number.find("XC") != -1:
        x += 90
        roman_number = roman_number.replace("XC", "")

    x += roman_number.count("C") * 100

    if roman_number.find("XL") != -1:
        x += 40
        roman_number = roman_number.replace("XL", "")

    x += roman_number.count("L") * 50

    if roman_number.find("IX") != -1:
        x + 9
        roman_number = roman_number.replace("IX", "")

    x += roman_number.count("X") * 10

    if roman_number.find("IV") != -1:
        x += 4
        roman_number = roman_number.replace("IV", "")

    x += roman_number.count("V") * 5

    x += roman_number.count("I")

    print x


roman_to_number()
