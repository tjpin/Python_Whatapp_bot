from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1> Welcome to whatsapp bot 2020 </h1>"

@app.route("/chats", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')

    # Create reply
    resp = MessagingResponse()
    resp.message(msg)

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)