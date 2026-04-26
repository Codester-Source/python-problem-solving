"""Moudle to cheack Armstrong numbers"""
def is_armstrong_number(number):
    """return if number is Armstrong or not"""
    pow_number = len(str(number))
    total_digits = 0
    for digit in str(number):
        digits_pow = int(digit) ** int(pow_number)
        total_digits+=digits_pow
    return total_digits == number  