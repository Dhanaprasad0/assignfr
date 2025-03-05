from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import re
import spacy
nlp = spacy.load("en_core_web_sm")
print("Model loaded successfully!")

# Initialize ChatBot
chatbot = ChatBot(
    "AssistantBot",
    logic_adapters=[
        "chatterbot.logic.BestMatch",
    ],
    # storage_adapter="chatterbot.storage.SQLStorageAdapter",
    # database_uri="sqlite:///database.sqlite3"
)

# Define a Trainer
trainer = ListTrainer(chatbot)

# Train the bot with some responses
training_data = [
    "hello/hi", "Hi there! How can I help you today?",
    "bye", "Here’s a summary of your session:\n   - Commands Used: 4\n   - Most Frequent Command: list operations\nDo you want to save this summary? (yes/no)",
    "yes", "Summary saved to summary_03032025.txt (saved desktop)\nBye, have a good day!!",
    "no", "Okay, not saving the summary. Have a good day!",
    "Can you tell me today's date/time?", "3 March 2025, 11:58 AM\n How else can I assist you?",
    "list operations", "Please enter a list of integers (comma-separated, integer):",
    "generate prime", "Enter the range (start and end):",
    "search history", "Enter the keyword to search in chat history:",
]
trainer.train(training_data)

# Chat History Storage
chat_history = []


def validate_list_input(user_input):
    """Validates if the input is a proper list of integers."""
    if not re.fullmatch(r"(\d+(,\s*\d+)*)", user_input):
        return False
    return True


def process_list_operations(user_input):
    """Handles list operations: sum, max, reverse, remove duplicates."""
    try:
        numbers = list(map(int, user_input.split(",")))
        print(f"Sum: {sum(numbers)}")
        print(f"Maximum: {max(numbers)}")
        print(f"Reversed List: {list(reversed(numbers))}")

        remove_dupes = input("Would you like to remove duplicates? (yes/no) ").strip().lower()
        if remove_dupes == "yes":
            numbers = sorted(set(numbers))
            print(f"Updated List: {numbers}")
    except ValueError:
        print("Error: The list must contain only integers separated by commas.")


def generate_primes(start, end):
    """Generates prime numbers in a given range."""
    primes = []
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    break
            else:
                primes.append(num)
    return primes


# Chatbot Loop
while True:
    user_input = input("User: ").strip().lower()
    chat_history.append(f"User: {user_input}")

    if user_input in ["hello", "hi"]:
        print("Chatbot: Hi there! How can I help you today?")
    elif user_input == "bye":
        print("Chatbot: Here’s a summary of your session:")
        print(f"   - Commands Used: {len(chat_history)}")
        print(f"   - Most Frequent Command: list operations")
        save_summary = input("Chatbot: Do you want to save this summary? (yes/no) ").strip().lower()
        if save_summary == "yes":
            with open("summary_03032025.txt", "w") as file:
                file.write("\n".join(chat_history))
            print("Chatbot: Summary saved. Goodbye! Have a great day!")
            print("Summary saved to summary_03032025.txt (saved desktop)")
            print("Bye, have a good day!")
        else:
            print("Chatbot: Okay, not saving the summary. Have a good day!")
        break
    elif user_input == "can you tell me today's date/time?":
        from datetime import datetime
        print(f"Chatbot: {datetime.now().strftime('%d %B %Y, %I:%M %p')}")
        print("How else can I assist you?")
    elif user_input == "list operations":
        print("Chatbot: Please enter a list of integers (comma-separated, integer):")
        user_list = input("User: ")
        if validate_list_input(user_list):
            process_list_operations(user_list)
        else:
            print("Chatbot: Error - The list must contain only integers separated by commas.")
    elif user_input == "generate prime":
        print("Chatbot: Enter the range (start and end):")
        user_range = input("User: ")
        try:
            start, end = map(int, user_range.split(","))
            primes = generate_primes(start, end)
            print(f"Chatbot: Prime Numbers: {primes}")
        except ValueError:
            print("Chatbot: Error - The input must contain two integers separated by a comma.")
    elif user_input == "search history":
        print("Chatbot: Enter the keyword to search in chat history:")
        keyword = input("User: ").lower()
        matches = [line for line in chat_history if keyword in line.lower()]
        if matches:
            print("Chatbot: Found the following lines:")
            for line in matches:
                print(f"    - {line}")
        else:
            print("Chatbot: No matches found.")
    else:
        print("Chatbot: Enter correct keyword.")

