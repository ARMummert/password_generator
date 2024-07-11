import random
import string

def generate_password(length, use_lowercase, use_uppercase, use_digits, use_special):
    alphabet = ''
    if use_lowercase:
        alphabet += string.ascii_lowercase
    if use_uppercase:
        alphabet += string.ascii_uppercase
    if use_digits:
        alphabet += string.digits
    if use_special:
        alphabet += string.punctuation
    return ''.join(random.choice(alphabet) for i in range(length))

length = int(input('Enter the length of the password: '))

use_lowercase = input('Use lowercase letters? (y/n): ')

use_uppercase = input('Use uppercase letters? (y/n): ')

use_digits = input('Use digits? (y/n): ')

use_special = input('Use special characters? (y/n): ')

print(generate_password(length, use_lowercase == 'y', use_uppercase == 'y', use_digits == 'y', use_special == 'y'))

