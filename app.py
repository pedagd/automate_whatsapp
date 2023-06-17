import ssl
from flask import flask, request
from twilio.twiml.messaging_response import MessagingResponse
from pymongo import MongoClient
from datetime import datetime

cluster = MongoClient("mongodb+srv://pdurgasankar:2CeGlXcfFysF8U0W@cluster0.t0usdtu.mongodb.net/")
db = cluster["Directory_Services"]
contacts = db["contacts"]
app = Flask(__name__)

@app.route("/", methods=["get","post"])
def reply():
    text = request.form.get("Body")
    number = request.form.get("From")
    number = number.replace("whatsapp:","")[:-2]
    
    response = MessagingResponse()
                      
    response.message("Hello Durga");
    return str(response)

if __name__ == "__main__":
    app.run()
