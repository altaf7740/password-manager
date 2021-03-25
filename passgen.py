import random

def get_alphanumeric_password(digit):
    
    password = ""
    for loop in range(digit):
        password = password + random.choice([chr(random.randint(48,57)),chr(random.randint(65,90)),chr(random.randint(97,122))])
    return password


def get_complex_password(digit):
    password = ""
    for loop in range(digit):
        password = password + chr(random.randint(33,127))
    return password


def get_lower_alpha_numeric_password(digit):
    
    password = ""
    for loop in range(digit):
        password = password + random.choice([chr(random.randint(48,57)),chr(random.randint(97,122))])
    return password


def get_upper_alpha_numeric_password(digit):
    
    password = ""
    for loop in range(digit):
        password = password + random.choice([chr(random.randint(48,57)),chr(random.randint(65,90))])
    return password


def get_upper_alpha_password(digit):
    
    password = ""
    for loop in range(digit):
        password = password +chr(random.randint(65,90))
    return password


def get_lower_alpha_password(digit):
    
    password = ""
    for loop in range(digit):
        password = password +chr(random.randint(97,122))
    return password

def get_numeric_password(digit):
    
    password = ""
    for loop in range(digit):
        password = password + chr(random.randint(48,57))
    return password
# ------------------------------------------------------------

def get_special_only_password(digit):
    
    password = ""
    for loop in range(digit):
        password = password + random.choice([chr(random.randint(33,47)),chr(random.randint(58,64)),chr(random.randint(91,96)),chr(random.randint(123,126))])
    return password

def get_special_upper_password(digit):
    
    password = ""
    for loop in range(digit):
        password = password + random.choice([chr(random.randint(33,47)),chr(random.randint(58,64)),chr(random.randint(91,96)),chr(random.randint(123,126)),chr(random.randint(65,90))])
    return password

def get_special_lower_password(digit):
    
    password = ""
    for loop in range(digit):
        password = password + random.choice([chr(random.randint(33,47)),chr(random.randint(58,64)),chr(random.randint(91,96)),chr(random.randint(123,126)),chr(random.randint(97,122))])
    return password

def get_special_numeric_password(digit):
    
    password = ""
    for loop in range(digit):
        password = password + random.choice([chr(random.randint(33,47)),chr(random.randint(58,64)),chr(random.randint(91,96)),chr(random.randint(123,126)),chr(random.randint(48,57))])
    return password

def get_upper_alphanumeric_special_password(digit):
    
    password = ""
    for loop in range(digit):
        password = password + random.choice([chr(random.randint(33,47)),chr(random.randint(58,64)),chr(random.randint(91,96)),chr(random.randint(123,126)),chr(random.randint(48,57)),chr(random.randint(65,90))])
    return password

def get_lower_alpha_numeric_special_password(digit):
    
    password = ""
    for loop in range(digit):
        password = password + random.choice([chr(random.randint(33,47)),chr(random.randint(58,64)),chr(random.randint(91,96)),chr(random.randint(123,126)),chr(random.randint(97,122)),chr(random.randint(48,57))])
    return password


def get_alpha_special_password(digit):
    
    password = ""
    for loop in range(digit):
        password = password + random.choice([chr(random.randint(33,47)),chr(random.randint(58,64)),chr(random.randint(91,96)),chr(random.randint(123,126)),chr(random.randint(65,90)),chr(random.randint(97,122))])
    return password

def get_alpha_password(digit):
    
    password = ""
    for loop in range(digit):
        password = password + random.choice([chr(random.randint(65,90)),chr(random.randint(97,122))])
    return password

