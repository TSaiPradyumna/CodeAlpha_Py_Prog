import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey!"]
    ],
    [
        r"how are you?",
        ["I'm doing well, thank you!", "I'm great, thanks for asking!"]
    ],
    [
        r"what is your name?",
        ["You can call me Chatbot.", "I'm Chatbot, nice to meet you!"]
    ],
    [
        r"want to ask a question",
        ["Yeah sure"]
    ],
    [
        r"(.*) your name(.*)",
        ["My name is Chatbot.", "I go by the name Chatbot."]
    ],
    [
        r"(.*) (sorry|apologies)(.*)",
        ["No need to apologize.", "It's alright."]
    ],
    [
        r"quit|bye|exit",
        ["Goodbye!", "Bye, take care!"]
    ],
    [
        r"how old are you?",
        ["I am just a computer program, so I don't have an age."]
    ],
    [
        r"what can you do?",
        ["I'm here to chat with you and answer your questions!"]
    ],
    [
        r"tell me a joke",
        ["Why don't scientists trust atoms? Because they make up everything!"]
    ],
    [
        r"(.*) (love|like) you(.*)",
        ["Aww, thank you!", "That's very kind of you!"]
    ],
    [
        r"(.*) (hate|dislike) you(.*)",
        ["I'm sorry to hear that."]
    ],
    [
        r"what is the weather today?",
        ["I'm just a chatbot and I can't check the weather. You can use a weather app or website to find out!"]
    ],
    [
        r"what is your favorite color?",
        ["I don't have a favorite color, as I am just a program."]
    ],
    [
        r"how can I help you?",
        ["You can ask me anything you'd like to know!"]
    ]
]

#Defining our Chatbot Function
def chatbot():
    print("Hi! I'm a basic chatbot. Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

#Calling out the function
if __name__ == "__main__":
    chatbot()