# rule_based_chatbot.py

def get_response(user_input):
    user_input = user_input.lower().strip()

    rules = {
        "hi": "Hello! How can I help you?", "thanks": "you are welcome",
        "hello": "Hi there! Need assistance with something?",
        "how are you": "I'm just code, but thanks for asking!",
        "who are you": "I’m a simple chatbot created by Girish!"
    }

    return rules.get(user_input, "Sorry, I didn't understand that.")


def start_chat():
    print("🤖 Chatbot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print(" Chatbot: Goodbye! 👋")
            break
        response = get_response(user_input)
        print(f"Chatbot: {response}")


if __name__ == "__main__":
    start_chat()
