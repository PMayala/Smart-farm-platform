import sqlite3
 class User:
def __init__(self,  user_id, name):
    self.user_id = user_id
    self.name
 def start_prompt(self):
   	choice = input("Are you a registered user? (yes/no): ").lower()

   	if choice == "yes":
       	username = input("Enter your username: ")
       	password = input("Enter your password: ")
       	if self.authenticate_user(username, password):
           	print(f"\nWelcome back, {username}!")
           	return username
       	else:
           	print("Invalid credentials. Please try again.\n")
           	exit()
   	elif choice == "no":
       	username = input("Enter a username: ")
       	password = input("Create a password: ")
       	self.register_user(username, password)
       	print("Registration successful! You can now log in.")
       	return username
   	else:
       	print("Invalid input. Please enter 'yes' or 'no'.\n")
       	exit()
