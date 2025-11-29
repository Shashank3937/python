from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
import yaml

chatbot = ChatBot("MyBot")

# Load custom YAML
with open("data/custom.yml", "r") as file:
    data = yaml.safe_load(file)

trainer = ListTrainer(chatbot)

# Extract conversations from YAML
for conv in data["conversations"]:
    trainer.train(conv)

print("Training complete!")
