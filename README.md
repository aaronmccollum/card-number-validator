# Card Number Validator
Credit card number validation script using the Luhn Algorithm

## Luhn Algorithm
The Luhn Algorithm is used to validate ID numbers, like credit card numbers. Additionally, because the final sum has to end in 0, you can use it to find a missing number or checksum.
1. From right to left, double every second digit. If product is greater than 9, sum the digits of the product and use that instead of the actual product.
2. Take the sum of all the digits
3. If the sum of all the digits divides evenly by 10 (i.e. if it ends in a 0), the number is valid. Otherwise, it is invalid.

## Python lessons learned:
- `str.maketrans({k: v, k: v, k: v})` takes k in str and replaces it with v
- `my_str.translate(str.maketrans())` returns the translated string

## Resources
Youtube lesson link: https://www.youtube.com/watch?v=PNXXqzU4YnM
freeCodeCamp lesson link: https://www.freecodecamp.org/learn/scientific-computing-with-python/
