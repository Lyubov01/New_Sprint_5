import random
import string

def gen_login(first_name, last_name, cogorta, domain = 'mail.ru'):
    random_login = str(random.randint(100,999))
    new_login = first_name.lower() + "_" + last_name.lower() + "_" + str(cogorta) + "_" + random_login + "@" + domain
    return new_login 

def gen_password():
    symbols = string.ascii_letters + string.digits
    password = ""
    for _ in range(6):
        password += random.choice(symbols)
    return password

email= gen_login ('lyubov', 'melnikova', 30)
print(email)