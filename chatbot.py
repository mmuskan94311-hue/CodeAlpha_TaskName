def chatbot():

    print("================================")
    print("        BASIC CHATBOT")
    print("================================")

    print("Chatbot: Hello! I am a simple Python chatbot.")
    print("Chatbot: Type 'bye' to exit.")

    while True:

        user_input = input("\nYou: ").lower().strip()

        if user_input == "hello" or user_input == "hi":
            print("Chatbot: Hi! Nice to meet you.")

        elif user_input == "how are you":
            print("Chatbot: I'm fine, thanks!")

        elif user_input == "what is your name":
            print("Chatbot: My name is Python Chatbot.")

        elif user_input == "what can you do":
            print("Chatbot: I can answer some basic questions.")

        elif user_input == "thank you" or user_input == "thanks":
            print("Chatbot: You're welcome!")

        elif user_input == "bye":
            print("Chatbot: Goodbye! Have a nice day!")
            break

        else:
            print("Chatbot: Sorry, I don't understand that.")


chatbot()