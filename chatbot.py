from datetime import datetime
import random

print("=" * 40)
print("        SMART PYTHON CHATBOT")
print("=" * 40)

jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why did the Python developer wear glasses? Because he couldn't C!",
    "Programming is 10% coding and 90% figuring out why it doesn't work."
]

while True:
    user = input("\nYou: ").lower()

    if user in ["hi", "hello", "hey"]:
        print("Bot: Hello! Nice to meet you.")

    elif "name" in user:
        print("Bot: I am a Python Chatbot created for the CodeAlpha Internship.")

    elif "how are you" in user:
        print("Bot: I'm doing great. Thanks for asking!")

    elif "time" in user:
        current_time = datetime.now().strftime("%I:%M %p")
        print("Bot: Current time is", current_time)

    elif "date" in user:
        current_date = datetime.now().strftime("%d-%m-%Y")
        print("Bot: Today's date is", current_date)

    elif "joke" in user:
        print("Bot:", random.choice(jokes))

    elif user in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! Have a wonderful day.")
        break

    else:
        print("Bot: Sorry, I don't understand that yet.")