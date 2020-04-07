from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from utils import find_response

app = Flask(__name__)

# Page view template........not that important, just to display something
@app.route("/")
def home_view():
    return "<h1> Welcome to whatsapp bot 2020 </h1>"


@app.route("/chats", methods=['POST'])
def chats_reply():
    # Respond to incoming calls with a simple text message.
    # Find and read messages
    p_number = request.form.get('From')
    msg = request.form.get('Body')
    reply = find_response(msg, p_number)

    # Find response

    resp = MessagingResponse()
    resp.message(reply)

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
