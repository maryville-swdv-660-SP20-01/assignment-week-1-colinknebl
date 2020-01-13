from passwordstrength.passwordmeter import PasswordStrength
from colorama import init, Fore, Style

def main():
    user_input = input('Enter password to test: ')

    strength = PasswordStrength(user_input)

    style = Style.BRIGHT
    color = None

    rating = strength.rating() # ratings: Very Weak, Weak, Good, Strong, Very Strong

    if 'Strong' in rating:
        color = Fore.GREEN

    elif 'Good' in rating:
        color = Fore.YELLOW

    else:
        color = Fore.RED
    
    print('Password Strength: ' + color + style + rating)


if __name__ == '__main__': 
    main()

