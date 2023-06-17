import ssl
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from pymongo import MongoClient
from datetime import datetime

cluster = MongoClient("mongodb+srv://pdurgasankar:2CeGlXcfFysF8U0W@cluster0.t0usdtu.mongodb.net/")
db = cluster["Directory_Services"]
contacts = db["contacts"]
users = db["users"]

app = Flask(__name__)

@app.route("/", methods=["get","post"])
def reply():
    text = request.form.get("Body")
    number = request.form.get("From")
   
    response = MessagingResponse()
    response.message("Welcome")
    
    try:        
        user = users.find_one({'number': number})
    except:
        response.message(" Error Occured While Fetching User")
        return str(response)
        
    return str(response)
if __name__ == "__main__":
    app.run()
