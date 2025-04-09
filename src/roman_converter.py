def decimal_to_roman(num):
    
    if not (1 <= num <= 3999):
        raise ValueError("Número fuera de rango (debe estar entre 1 y 3999)")

   
    roman_numerals = [
        ("M", 1000),
        ("CM", 900),
        ("D", 500),
        ("CD", 400),
        ("C", 100),
        ("XC", 90),
        ("L", 50),
        ("XL", 40),
        ("X", 10),
        ("IX", 9),
        ("V", 5),
        ("IV", 4),
        ("I", 1),
    ]

    resultado = []
    for roman, value in roman_numerals:
        while num >= value:
            resultado.append(roman)
            num -= value

    return ''.join(resultado)


