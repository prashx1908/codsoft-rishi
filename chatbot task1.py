import random

def get_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"

    elif "how are you" in user_input:
        return "I'm just a computer program, but thanks for asking!"

    elif "your name" in user_input:
        return "I'm a chatbot. You can call me ChatGPT."

    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day."

    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase or ask another question?"

def main():
    print("Rule-Based Chatbot: Hello! Type 'bye' to exit.")

    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'bye':
            print("Rule-Based Chatbot: Goodbye!")
            break

        response = get_response(user_input)
        print("Rule-Based Chatbot:", response)

if __name__ == "__main__":
    main()
