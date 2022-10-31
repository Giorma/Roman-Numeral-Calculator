ROMAN = [
    ( 100, "C"),
    (  90, "XC"),
    (  50, "L"),
    (  40, "XL"),
    (  10, "X"),
    (   9, "IX"),
    (   5, "V"),
    (   4, "IV"),
    (   1, "I"),
]
rom_val = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50, 'XC': 90, 'C': 100}
###### integer to roman numeral
def int_to_roman(number):
    result = ""
    for (arabic, roman) in ROMAN:
        (factor, number) = divmod(number, arabic)
        result += roman * factor
    return result
######

###### roman numeral to integer
def roman_to_int(s):
    s = s.upper()
    int_val = 0
    for i in range(len(s)):
        if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
            int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
        else:
            int_val += rom_val[s[i]]
    return int_val
######

def ValidationOfRomanNumerals(string):

    import re

    return (bool(re.search(r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$", string)))

###### calculator
result = 0

f = input("Enter Number: ")

while True:

    opera = input("Enter operator: +, -, *, /, to exit enter 0 : ")

    if opera == '0':
        print(f"Result is: {f}")
        break

    s = input("Enter Number: ")

    if ValidationOfRomanNumerals(f.upper()) != True or ValidationOfRomanNumerals(s.upper()) != True:
        print("Roman numeral not exist")
        break

    if opera == '+':
        result = roman_to_int(f) + roman_to_int(s)
        f = int_to_roman(result)

        print(f"Result is: {f}")

    elif opera == '-':
        result = roman_to_int(f) - roman_to_int(s)
        f = int_to_roman(result)
        print(f"Result is: {f}")

    elif opera == '*' or opera.lower() == 'x':
        result = roman_to_int(f) * roman_to_int(s)
        f = int_to_roman(result)
        print(f"Result is: {f}")

    elif opera == '/':
        result = roman_to_int(f) / roman_to_int(s)
        f = int_to_roman(int(result))
        print(f"Result is: {f}")

    else:
        print("Something is Wrong")
        break
######