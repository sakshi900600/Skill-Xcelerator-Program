import getpass

password = getpass.getpass("Enter your password: ")

print("Password length is", len(password), "characters (hidden for security).")


print(len(password) * '*')

# output:
# Enter your password: 
# Password length is 5 characters (hidden for security).