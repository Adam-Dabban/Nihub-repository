# import random
# from dotenv import load_dotenv
# from langchain_google_genai import ChatGoogleGenerativeAI


# load_dotenv()

# gemini = ['The mic is yours', 'Ask away', 'Any new ideas to explore', "What are we building today", "What should we focus on", "Ready when you are"]
# chill = random.choices(gemini)[0]
# # print(chill)
# name = input("What is your name ? :")
# print(f"🤖 Gemini : {chill} {name}")
# my_commands = [
#     "exit",
#     "quit"
# ]
# while True :
#     user_input = input("What is your question : ")
#     model = ChatGoogleGenerativeAI(model= "gemini-3.5-flash")
#     response = model.invoke(user_input)


#     if user_input.lower() in my_commands:
#         print("Goodbye!")
#         break
    

#     print(f"{response.text}\n")

# from numpy import random

# def start_game():
#     # Pick a secret number between 1 and 100
#     secret_number = random.randint(1, 100)
#     attempts = 0
    
#     print("=== Welcome to the Number Guessing Game! ===")
#     print("I'm thinking of a number between 1 and 100.")

#     while True:
#         try:
#             guess = int(input("Take a guess: "))
#             attempts += 1
            
#             if guess < secret_number:
#                 print("Too low! Try again.")
#             elif guess > secret_number:
#                 print("Too high! Try again.")
#             else:
#                 print(f"🎉 Correct! You found it in {attempts} attempts.")
#                 break
#         except ValueError:
#             print("Please enter a valid whole number.")

# if __name__ == "__main__":
#     start_game()

m = 10  # kg k
r = 2   # m
v = 50  # m/s

a_c = (v ** 2) / r
f_c = m * a_c

print(f"a_c = {a_c}")
print(f"f_c = {f_c}")
