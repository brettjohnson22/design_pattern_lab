from chat_history import chat_history

class User:
    def send_message(self, message):
        chat_history.messages.append(message)
