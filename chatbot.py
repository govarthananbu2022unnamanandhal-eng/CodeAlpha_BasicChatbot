# Simple Rule-Based Chatbot for CodeAlpha Internship

def chatbot_response(user_input):
    user_input = user_input.lower().strip()
    
    # Predefined rules and responses
    if user_input in ["hello", "hi", "hey"]:
        return "Hi there! How can I help you today?"
    elif user_input in ["how are you", "how are you?"]:
        return "I'm fine, thanks for asking! How about you?"
    elif user_input in ["what is your name", "what is your name?"]:
        return "I am a simple Python Chatbot created for CodeAlpha internship."
    elif user_input in ["bye", "goodbye"]:
        return "Goodbye! Have a great day ahead!"
    else:
        return "I'm sorry, I don't understand that. Try saying 'hello', 'how are you', or 'bye'."

# Main Chat Loop
print("--- Welcome to Basic Chatbot ---")
print("Type 'bye' to exit the chat.\n")

while True:
    user_message = input("You: ")
    
    if user_message.lower().strip() == "bye":
        print("Chatbot: Goodbye! Have a great day ahead!")
        break
        
    response = chatbot_response(user_message)
    print("Chatbot:", response)
  
