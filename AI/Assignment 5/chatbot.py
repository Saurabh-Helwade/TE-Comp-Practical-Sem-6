import random

def get_bot_response(user_input):
    responses = {
        "hello": "Hi there! How can I help you?",
        "how are you": "I'm just a computer program, but thanks for asking!",
        "bye": "Goodbye! Have a great day!",
        "default": "I'm sorry, I don't understand that. Can you please rephrase?",
        "what are the best colleges from pune?": [
        "COEP",
        "PICT",
        "VIT",
        "CUMMINS",
        "PCCOE"
    ],

    "which are the best engineering branches?" : [
        "Computer Engineering",
        "IT Engineering",
        "ENTC Engineering"
    ],

    "what are the top branch cut-offs for coep?" : [
        "Computer Engineering : 99.8 percentile",
        "Does not have IT branch",
        "ENTC Engineering: 99.2 percentile"
    ],   

    "what are the top branch cut-offs for pict?" : [
        "Computer Engineering : 99.4 percentile",
        "IT Engineering : 98.6 percentile",
        "ENTC Engineering: 97.2 percentile"
    ],  

    "what are the top branch cut-offs for vit?" : [
        "Computer Engineering : 99.8 percentile",
        "IT Engineering: 97.1 percentile",
        "ENTC Engineering: 96.2 percentile",
    ],    

    "what are the top branch cut-offs for cummins?" : [
        "Computer Engineering : 99.8 percentile",
        "Does not have IT branch",
        "ENTC Engineering: 99.2",
    ],  

    "what are the top branch cut-offs for pccoe?" : [
        "Computer Engineering : 99.8 percentile",
        "Does not have IT branch",
        "ENTC Engineering: 99.2"
    ], 

    "when do college admissions start?": ["Admissions generally start around August"],
        
    }

    return responses.get(user_input.lower(), responses["default"])

def main():
    print("Welcome to the Simple Chatbot!")
    print("This is chatbot for college inquery!")

    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'exit':
            print("Goodbye! Have a great day!")
            break

        bot_response = get_bot_response(user_input)
        print("Bot:", bot_response)

if __name__ == "__main__":
    main()
