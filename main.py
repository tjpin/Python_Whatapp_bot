from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from utils import fetch_reply

app = Flask(__name__)


@app.route("/")
def hello():
    return "<h1> Welcome to whatsapp bot 2020 </h1>"


@app.route("/chats", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')
    p_number = request.form.get('From')
    reply = fetch_reply(msg, p_number)

    # Create reply

    resp = MessagingResponse()
    resp.message(reply)

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
