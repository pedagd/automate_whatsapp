import ssl
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from pymongo import MongoClient
from datetime import datetime

cluster = MongoClient("mongodb+srv://pdurgasankar:2CeGlXcfFysF8U0W@cluster0.t0usdtu.mongodb.net/Directory_Services?retryWrites=true&w=majority")
db = cluster["Directory_Services"]
contacts = db["Contacts"]
users = db["users"]

app = Flask(__name__)

@app.route("/", methods=["get","post"])
def reply():
    text = request.form.get("Body")
    number = request.form.get("From")
    number = number.replace("whatsapp:", "")

    msg = "Hi {0}, Thanks for reaching Local Directory Service. \n Choose from the options below:\n\n*Type*\n\n"
    response = MessagingResponse()
    
    for x in contacts.find():
        msg += "*{0}* - {1}\n".format(x["slno"],x["type"])    
    
    response.message(msg)
    
    try:
       option = int(text)
    except:
       response.message.clear()
       response.message("Hi {0}, Thanks for reaching Local Directory Service. \n Choose from the options below:"
                           "\n\n*Type*\n\n {1}".format(number,msg))
       return str(response)
    
    if bool(option) == True:
        try:            
            contact = contacts.find_one({"slno": option})
            if bool(contact) == True:
                response.message.clear()
                response.message("Name:{0}\nNumber:{1}\nRemarks:{2}\nRating:{3}".format(
                contact["name"], contact["number"], contact["remarks"], contact["ratings"]))
                return str(response)
            else:
                response.message("Unable to find contact - from else")
                return str(response)
        except:
            response.message("Unable to find contact")
            return str(response)
    else:
        response.message(msg)
    
    return str(response)
    
if __name__ == "__main__":
    app.run()
