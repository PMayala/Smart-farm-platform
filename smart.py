import time

class User:
    def __init__(self, name):
        self.name = name
        self.progress = {"Educational Modules": 0, "Q&A Sessions": 0, "Job Applications": 0}


         def introduction(self):
             print("Welcome to the Smart Farming Platform!")
             print("Our mission is to empower farmers through education, collaboration, and employment opportunities.")
            print("Let's embark on this journey together!\n")

            def educational_module(self, user):
        print("\n=== Educational Modules ===")
        print("1. Modern Farming Techniques")
        print("2. Sustainable Practices")
        choice = input("Enter the number of the module you want to explore: ")


        if choice == "1":
            print("\n=== Modern Farming Techniques ===")
            print("Check out the following resources:")
            print("1. Article: Introduction to Precision Agriculture - https://extension.missouri.edu/publications/wq450")
            print("2. Video: Advanced Irrigation Techniques - https://youtu.be/Z9HAy9EYKKs?feature=shared")
            user.progress["Educational Modules"] += 1
        elif choice == "2":
            print("\n=== Sustainable Practices ===")
            print("Explore the following materials:")
            print("1. Article: Sustainable Crop Rotation Strategies - https://sustainablereview.com/sustainable-crop-rotation-practices/")
            print("2. Video: Organic Farming Methods - https://youtu.be/WhOrIUlrnPo?feature=shared")
            user.progress["Educational Modules"] += 1
        else:
            print("Invalid choice. Please enter a valid module number.")

    def qna_interaction(self, user):

