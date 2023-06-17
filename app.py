import ssl
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from pymongo import MongoClient
from datetime import datetime

#cluster = MongoClient("mongodb+srv://pdurgasankar:2CeGlXcfFysF8U0W@cluster0.t0usdtu.mongodb.net/")
cluster = MongoClient("mongodb+srv://pdurgasankar:2CeGlXcfFysF8U0W@cluster0.t0usdtu.mongodb.net/?retryWrites=true&w=majority")
db = cluster["Directory_Services"]
contacts = db["contacts"]
users = db["users"]

app = Flask(__name__)

@app.route("/", methods=["get","post"])
def reply():
    text = request.form.get("Body")
    number = request.form.get("From")
    number = number.replace("whatsapp:", "")
    response = MessagingResponse()
    response.message("Welcome {0}".format(number))
    
    #try:        
    #   user = users.find_one({'number': number})
    #except:
    #    response.message(" Error Occured While Fetching User")
    #    return str(response)
        
    return str(response)
    
if __name__ == "__main__":
    app.run()
