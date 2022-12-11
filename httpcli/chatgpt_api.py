"""
   File Name :    chatgpt_api.py
   Description :
   Author :       Cl0udG0d
   date :         2022/12/11
"""
from revChatGPT.revChatGPT import Chatbot

# For the config please go here:
# https://github.com/acheong08/ChatGPT/wiki/Setup
config = {
    # "email": "",
    # "password": "",
    "session_token": "", # Deprecated. Use only if you encounter captcha with email/password
    #"proxy": "<HTTP/HTTPS_PROXY>"
}


chatbot = Chatbot(config, conversation_id=None)

def test():
    response = chatbot.get_chat_response("Hello world", output="text")
    print(response)

if __name__ == '__main__':
    test()