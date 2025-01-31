from flask import Flask, request, jsonify
from twilio.rest import Client

app = Flask(__name__)

# Your Twilio credentials
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
from_whatsapp_number = 'whatsapp:+14155238886'  # Twilio's sandbox number or your own
client = Client(account_sid, auth_token)

@app.route('/send-message', methods=['POST'])
def send_message():
    # Get the recipient number and message from the request
    to_whatsapp_number = request.json.get('to')
    message_body = request.json.get('message')

    if not to_whatsapp_number or not message_body:
        return jsonify({'error': 'Please provide both "to" and "message" fields.'}), 400

    # Send the message via WhatsApp using Twilio
    try:
        message = client.messages.create(
            body=message_body,
            from_=from_whatsapp_number,
            to=f'whatsapp:{to_whatsapp_number}'
        )
        return jsonify({'status': 'success', 'message_sid': message.sid}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)