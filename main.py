user_name = input("What is your user name? ")
password = input("What is your password? ")

password_length = len(password)
hidden_password = '*' * password_length

print(f"Hey, {user_name} your password {hidden_password} is {password_length} letters long")