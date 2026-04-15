import random
import string
def generate_password(length=10):
    lowercase=string.ascii_lowercase
    uppercase=string.ascii_uppercase
    digits=string.digits
    all_chars=lowercase+uppercase+digits
    password=[
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits)
    ]
    for _ in range(length-3):
        password.append(random.choice(all_chars))
    random.shuffle(password)
    return ''.join(password)
print("Generated Password:", generate_password(12))