## Inteiro para Romano
def int_to_roman(num):
    """

    https://www.w3resource.com/python-exercises/class-exercises/python-class-exercise-1.php
    :param num:
    :return:
    """
    lookup = [
        (1000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I'),
    ]
    res = ''
    for (n, roman) in lookup:
        (d, num) = divmod(num, n)
        res += roman * d
    return res




## Romano para Inteiro


def roman_to_int(s):
    """
    https://www.tutorialspoint.com/roman-to-integer-in-python
    :type s: str
    :rtype: int
    """
    roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
        'IV': 4,
        'IX': 9,
        'XL': 40,
        'XC': 90,
        'CD': 400,
        'CM': 900
    }

    i = 0
    num = 0
    while i < len(s):
        if i + 1 < len(s) and s[i:i + 2] in roman:
            num += roman[s[i:i + 2]]
            i += 2
        else:
            # print(i)
            num += roman[s[i]]
            i += 1
    return num


if __name__ == '__main__':
    # Para testes
    print(int_to_roman(1))
    print(int_to_roman(156))
    print(roman_to_int('III'))
    print(roman_to_int('CDXLIII'))
