from flask import Flask, request
from twilio.twiml.messaging_response import Message, MessagingResponse
from sendAlertMessage import * 

app = Flask(__name__)


def possibleResponses(input):
    response = None
    if input == 'options':
        response = 'Welcome to Twext! Type in a keyword for the information:\n ' + 'Wildfire: For wildfire updates near you \n' +'WildfireTweet: For recent tweets about the wildfire near you.\n'+'Events: For Events happening near you\n' +'Safety: For safety updates near you (missing person, tragic event, etc)\n'
    elif input == 'Wildfire':
        response = finalMessage
    elif input == 'WildfireTweet':
        response = warning
    elif input == 'Events' or input == 'Safety':
        response = 'This feature is under construction'
    else:
        response = 'Invalid input, please try again or text options. '
    return response

@app.route('/sms', methods=['POST'])    
def sms():
    number = request.form['From']
    message_body = request.form['Body']

    # resp = MessagingResponse()
    # resp.message('Hello {}, you said: {}'.format(number, message_body))
    # return str(resp)
    sendingMessage = possibleResponses(str(message_body))
    resp = MessagingResponse()
    resp.message(sendingMessage)
    return str(resp)

if __name__ == '__main__':
    app.run()