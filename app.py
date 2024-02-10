# Verification helper function used in main()
def verify_card_number(card_number):
    sum_of_odd_digits = 0
    # Reverse the card number
    card_number_reversed = card_number[::-1]
    odd_digits = card_number_reversed[::2]

    # Sum all odd digits in reversed card number
    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    # Sum all even digits in reversed card number
    # If product is greater than 9, add the two digits together instead of the product
    sum_of_even_digits = 0
    even_digits = card_number_reversed[1::2]
    for digit in even_digits:
        number = int(digit) * 2
        if number >= 10:
            number = (number // 10) + (number % 10)
        sum_of_even_digits += number

    # Sum odds and evens together
    total = sum_of_odd_digits + sum_of_even_digits

    # Return True if valid, False if not valid
    return total % 10 == 0

# Main function that takes a card number, removes spaces and dashes, and verifies the number
def main():
    card_number = '4111-1111-4555-1142'
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

    if verify_card_number(translated_card_number):
        print('VALID!')
    else:
        print('INVALID!')

main()
