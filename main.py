from user import User
from credidentials import Credidential


def create_user(username, password):
    '''
    function that creates a user using a password and username
    '''
    new_user = User(username, password)
    return new_user


def login(username, password):
    user_login = Credidential.verify(username, password)
    return user_login


def save_newuser(user):
    '''
    function that saves a new user
    '''
    User.addUser(user)


def display_user(user):
    '''
    function that displays user
    '''
    return User.displayUser()


def delete_user(user):
    '''
    function that deletes user
    '''
    
    User.deleteUser()


def create_credential(accountType, username, password):
    '''
    function that create new credential details for a new user
    '''
    new_credential = Credidential(accountType, username, password)
    return new_credential


def delete_credential(credidentials):
    '''
    function that deletes credentials from the credential list
    '''
    Credidential.deleteCred(credidentials)


def if_exist(accountType):
    '''
    function that checks if the credentials of the searched name exist and return true or falsd
    '''
    return Credidential.if_exist(accountType)


def save_credentials(credidentials):
    '''
    function that addes a new credential to the credential
    '''
    Credidential.addCred(credidentials)


def find_credential(accountType):
    """
    Function that finds a Credentials by an account name and returns the Credentials that belong to that account
    """
    return Credidential.findcred(accountType)


def generate_pass(self):
    ''' 
    function tht generates password randomly
    '''
    generated_pass = User.generate_password(self)
    return generated_pass


def main():
    print("hello iam password locker iam glad to be of service \n" + '*'*50)
    option = input("select: \n 1 to Create account \n 2 to login \n")

    if int(option) == 1:

        print("Sigh up  \n" + '*'*100)
        username = input("Enter user name:")
        password = ""

        while True:
            pass_choice = input(
                "Enter 1 to autogenerate password \n Enter 2 to type your password")
            if int(pass_choice) == 1:
                password = generate_pass(password)
                break
            elif int(pass_choice) == 2:
                password = input("Type your password: \n")
                break
            else:
                print("invalid input!!!!")

        save_newuser(create_user(username, password))

        print("\n your account has been created successfully \n" + '*'*80 + '\n' +
              f"your username is {username}  your password {password} \n"+'*'*80)

    elif int(option) == 2:
        username = input("enter user name: ")
        password = input("enter password: ")

        login(username, password)

        if login:
            print(f" welcome to password locker {username}")
    else:
        print("Invalid input!!!!!")

    while True:
        print("To continue: \n select 1 to find credidentials \n select 2 to create new credidential \n select 3 to delete credidentials \n select 4 to exit")
        option = input("\n your choice: ")
        if int(option) == 1:
            accountType = input("enter the account to find")
            if find_credential(accountType):
                cred = find_credential(accountType)
                print(
                    f"user name is {cred.username} \n \n password is {cred.password} ")

            else:
                print("credidentials doesn't exist")
        elif int(option) == 2:

            accountType = input("enter the account \n")
            username = input("Enter username")
            password = ""

            while True:
                pass_choice = input(
                    "Enter 1 to autogenerate password: \n Enter 2 to type your password: \n")
                if int(pass_choice) == 1:
                    password = generate_pass(password)
                    break
                elif int(pass_choice) == 2:
                    password = input("Type your password: \n")
                    break
                else:
                    print("invalid input!!!!")

            save_credentials(create_credential(accountType, username, password))
            cred = find_credential(accountType)
            print(f"credentials for : {cred.accountType} successfully saved!!!")
            break
        elif int(option) == 3:
            print("Enter account name of the Credentials you want to delete")
            
            if find_credential(accountType):
                searched_cred = find_credential(accountType)
                print("_"*60)
                searched_cred. delete_credential()
                print('\n')
                print(f"Your stored credentials for : {searched_cred.account} successfully deleted!!!")
                print('\n')
                break
            else:
                print("The Credential you want to delete does not exist")
                break

        elif int(option) == 4:
             print(f"it was a pleasure having you here {username} see you another time amigo")
             break




if __name__ == '__main__':
    main()
