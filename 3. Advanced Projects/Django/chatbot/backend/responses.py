def bot_response(message):
    if message == "Hello":
        return "Hello! How can I assist you today?"
    elif message == "What is your name?":
        return "I am a <b><i>chatbot</i></b> created to assist you."
    else:
        return "I'm sorry, I don't understand that."