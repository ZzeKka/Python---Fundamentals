PASSWORDS = {
    'cadela' : 'cao321',
    'geraldo1998' : '111000',
    'golem' : '123rock321'
}

def pass_match():
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()
    if password == PASSWORDS.get(username):
        print('User logged in successfully')
    else:
        print('Login failed')
        
pass_match()