from user import User
from chat_history import chat_history

user_one = User()
user_two = User()

user_one.send_message("Hello.")
user_two.send_message("Hi.")
user_one.send_message("What are you doing this weekend?")
user_two.send_message("Camping in the Rocky Mountains.")
user_one.send_message("Sounds exciting. Be safe!")
chat_history.display_history()