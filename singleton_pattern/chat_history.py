class ChatHistory:
    def __init__(self) -> None:
        self.messages = []

    def display_history(self):
        for message in self.messages:
            print(message)

# This single instantiation of the ChatHistory class 
# is imported into both user and singleton_wrapper class
# Each separate user adds their messages to this object
# And the wrapper class displays all messages left by users
chat_history = ChatHistory()