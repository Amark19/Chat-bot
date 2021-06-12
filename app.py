from chatbot import chatbot
from flask import Flask, render_template, request
import pyttsx3
value=0

app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/voice")
def VoiceRecog():
    userText = request.args.get('msg')
    # return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    # print(userText)
    
    return str(chatbot.get_response(userText))
    # if value==1:
@app.route("/toaudio")
def toaudio():
    reply = request.args.get('msg')
    reply_witho_dot=""
    for i in range(len(reply)):
        if reply[i]!=".":
            reply_witho_dot+=reply[i]
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    volume=engine.getProperty('volume')   # getting details of current speaking rate 
    engine.setProperty('rate', 125)
    engine.setProperty('volume', 300)
    value=1
    engine.say(reply_witho_dot)
    engine.runAndWait()
    return str(1)

if __name__ == "__main__":
    app.run(debug=True)
   
        