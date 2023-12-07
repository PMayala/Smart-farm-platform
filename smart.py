import sqlite3
class User:
    def __init__(self, user_id, name):
       	self.user_id = user_id
       	self.name = name
       	self.progress = {"Educational Modules": 0, "Q&A Sessions": 0, "Job Applications": 0}

class SmartFarmingPlatform:
    def __init__(self):
       	self.users = {}
       	self.notifications = []
       	self.db_connection = sqlite3.connect('smart_farming.db')

    def create_tables(self):
   	with self.db_connection:
       	cursor = self.db_connection.cursor()
       	cursor.execute('''
           	CREATE TABLE IF NOT EXISTS users (
               	id INTEGER PRIMARY KEY AUTOINCREMENT,
               	username TEXT NOT NULL,
               	password TEXT NOT NULL
           	)
       	''')

    def register_user(self, username, password):
        with self.db_connection:
            cursor = self.db_connection.cursor()
            cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))

    def authenticate_user(self, username, password):
         with self.db_connection:
             cursor = self.db_connection.cursor()
             cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
             user_data = cursor.fetchone()
             return user_data is not None

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
    def main(self):
   	self.introduction()
   	username = self.start_prompt()
   	if username not in self.users:
       	self.users[username] = User(username, username)
   	user = self.users[username]
        while True:
       	self.display_dashboard()
       	choice = input("\nEnter the number of your choice:")
       	if choice == "1":
           	self.educational_module(user)
       	elif choice == "2":
           	self.qna_interaction(user)
       	elif choice == "3":
           	self.job_portal(user)
       	elif choice == "4":
           	self.check_progress(user)
       	elif choice == "5":
           	self.display_notifications()
       	elif choice == "6":
           	print(f"Thank you for exploring our Smart Farming Platform. Have a great day!")
           	break
       	else:
           	print("Invalid choice. Please enter a number from 1 to 6.\n")
   


