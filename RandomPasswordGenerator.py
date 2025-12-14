import random
import string

def generate_password(length, use_letters, use_numbers, use_symbols):
    character_pool = ""

    if use_letters:
        character_pool += string.ascii_letters   
    if use_numbers:
        character_pool += string.digits          
    if use_symbols:
        character_pool += string.punctuation    

    if not character_pool:
        raise ValueError("Error: You must select at least one character type!")

    password = "".join(random.choice(character_pool) for _ in range(length))
    return password


def main():
    print("----------Random Password Generator----------")

    while True:
        try:
            length = int(input("Enter password length (e.g., 12): "))
            if length <= 0:
                print("Length must be a positive number.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    use_letters = input("Include letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    try:
        password = generate_password(length, use_letters, use_numbers, use_symbols)
        print("\nYour generated password:")
        print(password)
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
