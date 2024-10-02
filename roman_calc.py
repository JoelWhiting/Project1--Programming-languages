#!/usr/bin/env python3
import re
import argparse

# Mapping of Roman numerals to integers
roman_to_int_map = {
    'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
}

# Mapping of integers to Roman numerals
int_to_roman_map = [
    (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
    (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
    (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
]

def is_valid_roman(roman):
    """
    Validates a Roman numeral string.
    
    Args:
        roman (str): Roman numeral string to validate.
        
    Returns:
        bool: True if valid Roman numeral, False otherwise.
    """
    pattern = "^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"
    return bool(re.match(pattern, roman))

def roman_to_int(roman):
    """
    Converts a Roman numeral string to its integer representation.
    
    Args:
        roman (str): Roman numeral string.
    
    Returns:
        int: Integer value of the Roman numeral.
    
    Raises:
        ValueError: If the input is not a valid Roman numeral.
    """
    # Check if the input is empty or invalid
    if not roman or not is_valid_roman(roman):
        raise ValueError(f"Invalid Roman numeral: '{roman}'")
    
    total = 0
    prev_value = 0
    for char in reversed(roman):
        current_value = roman_to_int_map[char]
        if current_value < prev_value:
            total -= current_value
        else:
            total += current_value
        prev_value = current_value
    return total

def int_to_roman(number):
    """
    Converts an integer to its Roman numeral representation.
    
    Args:
        number (int): Integer value to convert to Roman numeral.
    
    Returns:
        str: Roman numeral representation of the integer.
    """
    if number <= 0:
        return "0 does not exist in Roman numerals."
    if number > 3999:
        return "You’re going to need a bigger calculator."
    
    result = ''
    for value, numeral in int_to_roman_map:
        while number >= value:
            result += numeral
            number -= value
    return result

def calculate(expression):
    """
    Evaluates a mathematical expression that includes Roman numerals and returns the result as a Roman numeral.
    
    Args:
        expression (str): Mathematical expression containing Roman numerals.
    
    Returns:
        str: The result of the evaluated expression as a Roman numeral, or an error message if applicable.
    """
    # Remove spaces and handle parentheses and brackets
    expression = expression.replace("[", "(").replace("]", ")")

    # Convert Roman numerals in the expression to integers
    try:
        expression = re.sub(r'[IVXLCDM]+', lambda x: str(roman_to_int(x.group())), expression)
    except ValueError:
        return "I don’t know how to read this."

    try:
        # Evaluate the expression
        result = eval(expression)

        if result < 0:
            return "Negative numbers can’t be represented in Roman numerals."
        elif result == 0:
            return "0 does not exist in Roman numerals."
        elif result != int(result):
            return "There is no concept of a fractional number in Roman numerals."
        elif result > 3999:
            return "You’re going to need a bigger calculator."
        
        # Convert the result back to a Roman numeral
        return int_to_roman(int(result))
    except Exception:
        return "I don’t know how to read this."

def main():
    """
    Main function to parse arguments and evaluate the Roman numeral expression.
    """
    parser = argparse.ArgumentParser(description='Evaluate a mathematical expression involving Roman numerals.')
    parser.add_argument('expression', nargs='+', help='Enter a Roman numeral expression as separate arguments')
    args = parser.parse_args()

    # Join all parts of the input into a single expression string
    expression = ''.join(args.expression)

    # Check if the input is a standalone Roman numeral
    try:
        if is_valid_roman(expression):
            print(roman_to_int(expression))
        else:
            # Otherwise, calculate the result of the expression
            result = calculate(expression)
            print(result)
    except ValueError:
        print("I don’t know how to read this.")

if __name__ == "__main__":
    main()
