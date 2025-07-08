import random  #will give random numbers to generate password
import string  #will give string characters to generate password

def get_user_preferences():
    print("Welcome to the Random Password Generator!\n")

    while True:
        try:
            length = int(input("Enter desired password length (minimum 8): "))     #password should be at least 8 characters for security
            if length < 8:
                print("Password should be at least 8 characters long.")
                continue

            break

        except ValueError:
            print("Please enter a valid number.")

    include_letters = input("Include letters? (y/n): ").lower() == 'y'
    include_digits = input("Include digits? (y/n): ").lower() == 'y'
    include_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    if not (include_letters or include_digits or include_symbols):
        print("At least one character type should be selected.")

        return get_user_preferences()
    return length, include_letters, include_digits, include_symbols

def generate_password(length, use_letters, use_digits, use_symbols):
    characters = ""

    if use_letters:
        characters += string.ascii_letters  # a-z A-Z
    if use_digits:
        characters += string.digits         # 0-9
    if use_symbols:
        characters += string.punctuation    # !@#$%^&*

    if not characters:
        return "No characters selected."
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    length, use_letters, use_digits, use_symbols = get_user_preferences()
    password = generate_password(length, use_letters, use_digits, use_symbols)
    print(f"\nYour generated password is:\n{password}\n")

if __name__ == "__main__":
    main()






