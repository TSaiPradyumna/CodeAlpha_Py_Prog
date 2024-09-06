import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey! How can I assist you?"]
    ],
    [
        r"how are you?",
        ["I'm just a computer program, but thanks for asking!", "I'm doing well, how about you?"]
    ],
    [
        r"what is your name?",
        ["I am a simple chatbot created to help you.", "You can call me ChatBot!"]
    ],
    [
        r"quit",
        ["Goodbye! Have a nice day!", "See you later!"]
    ],
    [
        r"(.*)",
        ["I'm sorry, I don't understand that.", "Can you say that differently?"]
    ]
]


def chatbot():
    print("Hi! I'm a simple chatbot. Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()


if __name__ == "__main__":
    chatbot()