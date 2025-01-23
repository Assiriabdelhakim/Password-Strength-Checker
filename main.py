
Password  = input("Enter the password you want to check : ")

def password_with_special_chars(password):
    special_characters = "!\"#$%&'()*+,-./:;<= >?@[\\]^_`{|}~"
    counter = 0
    for char in password:
          if char in special_characters:
            counter = counter + 1
            
    if counter > 0:
        return password
    else:
        print("Your password doesn't contain any special caracter")
        return 0


def password_legnth(password):
    if len(password)< 12:
        print("the password should at least be 12 caracters")
        return 0
    else:
        return password

def passowrd_is_digits(password):
    if password.isdigit():
        print("the pasaword contain only digits, you should include mltiple type of caracters")
        return 0
    else:
        return password 
    
def password_with_lower(password):
    counter = 0
    for char in password:
        if char.islower():
            counter += 1
            break
        else:
            counter = 0
    if counter == 1:
        return password
    else:
        print("Your password doesn't contain any lowacase")
        return 0
    
def password_with_upper(password):
    counter = 0
    for char in password:
        if char.isupper():
            counter += 1
            break
        else:
            counter = 0
    if counter == 1:
        return password
    else:
        print("Your password doesn't contain any uppercase")
        return 0


score = 0
if password_legnth(Password) == Password:
    score += 1
if passowrd_is_digits(Password) == Password:
    score += 1
if password_with_lower(Password) == Password:
    score += 1
if password_with_upper(Password) == Password:
    score += 1
if password_with_special_chars(Password) == Password:
    score += 1

print("-------------------")
match score:
        case 1 | 2:
            print("Weak password ")
        case 3 | 4:
            print("moderate password")
        case 5:
            print("Strong password")
        case '_':
            print("Weak password ")

print("-------------------")



