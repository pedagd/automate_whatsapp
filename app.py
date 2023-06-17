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
    
    response.message("Hi {0}, Thanks for reaching Local Directory Service.\n Choose from the options below:"
                    "\n\n*Type*\n\n 1️⃣ - Water Softener \n 2️⃣ - Bike Puncture Service \n 3️⃣ - House Keeping Service".format(number))
    return str(response)
    
    try:
       option = int(text)
    except:
       response.message("Please enter a valid response")
       return str(response)            
    if option == 1:
        contact = contacts.find_one({"name": "Water Softener"})
        if bool(contact) == True:
            response.message("Name:{0}\nNumber:{1}\nRemarks:{2}\nRating:{3}".format(
            contact["name"], contact["number"], contact["remarks"], contact["ratings"]))
        else:
            response.message("Unable to find contact")
    else:
        response.message("Hi {0}, Thanks for reaching Local Directory Service.\n Choose from the options below:"
                    "\n\n*Type*\n\n 1️⃣ - Water Softener \n 2️⃣ - Bike Puncture Service \n 3️⃣ - House Keeping Service".format(user["name"]))
            
    return str(response)
    
if __name__ == "__main__":
    app.run()
