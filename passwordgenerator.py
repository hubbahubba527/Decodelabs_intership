import random
import string

length = int(input("Enter password length: "))

if length < 3:
    print("Password length must be at least 3.")
else:
    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits)
    ]

    characters = string.ascii_letters + string.digits

    for i in range(length ):
        password.append(random.choice(characters))

    random.shuffle(password)

    print("Generated Password:", "".join(password))
