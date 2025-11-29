from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
import spacy

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Create chatbot
chatbot = ChatBot(
    "MyBot",
    logic_adapters=[
        "chatterbot.logic.BestMatch"
    ]
)

# Optional: train custom data
custom_data = [
    "Hello",
    "Hi there!",
    "How are you?",
    "I'm fine, thank you.",
    "What is your name?",
    "My name is MyBot."
]

trainer = ListTrainer(chatbot)
trainer.train(custom_data)

print("Bot is ready! Type something...")

while True:
    user = input("You: ")
    if user.lower() in ["bye", "exit", "quit"]:
        print("Bot: Goodbye!")
        break
    response = chatbot.get_response(user)
    print("Bot:", response)
