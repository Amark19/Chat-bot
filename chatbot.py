from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

# Creating ChatBot Instance
chatbot = ChatBot(
    'CoronaBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch',
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand. I am still learning.',
            'maximum_similarity_threshold': 0.90
        }
    ],
    database_uri='sqlite:///database.sqlite3'
) 
 # Training with Personal Ques & Ans 

conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I am doing good!",
    "Want to contact admin",
    "Here is the mail for adminstrator xyz@gmail.com",
    "Thank you.",
    "You're welcome.",
    "I am not able to login",
    "Please check again that you have entered valid credentials and do remember password field is case sensitive.If you have forgot the password.you can change your passwoord in link mentioned there.",
    "Can't see downloaded files in my phone",
    "Please check your files in phonestorage/downloads in your phone.But still its recommended to use desktop.",
    "I have forgot the password",
    "You can change your password by clicking on forget link on login page.",
    "Is it necessary to create account",
    "No its not mandatory but you will be notify about our updates through mail and you can have better experience after creating account.",
    "I have not received confirmation sms for my payment.",
    "Please check again or wait for 24 hours if it's not received then also  you can just contact +91999999999 number"
    
]

trainer = ListTrainer(chatbot)
trainer.train(conversation)
# response=chatbot.get_response("I am not able to login")
# print(response)
# Training with English Corpus Data 
trainer_corpus = ChatterBotCorpusTrainer(chatbot)
trainer_corpus.train('chatterbot.corpus.english') 