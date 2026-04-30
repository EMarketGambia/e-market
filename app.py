from flask import Flask, request, jsonify
import requests
import hmac
import hashlib

app = Flask(__name__)

# --- YOUR CONFIGURATION ---
# Replace with your actual key from Wave Business Dashboard
WAVE_API_KEY = "your_wave_api_key_here" 
# Your WhatsApp number (The one you gave me)
MY_NUMBER = "2202071291" 

@app.route('/')
def home():
    return "E-Market Gambia Server is Running!"

# This is the "Automated Mode" for Wave payments
@app.route('/wave-webhook', methods=['POST'])
def wave_payment_webhook():
    # 1. Get the data from Wave
    data = request.json
    
    # 2. Check if payment was successful
    if data.get('type') == 'checkout.succeeded':
        amount = data['amount']
        currency = data['currency']
        
        # 3. AUTOMATION: Send the message to you on WhatsApp
        # This uses a simple notification log for now
        print(f"💰 SUCCESS: Received {amount} {currency} via Wave!")
        
        # In a real setup, we'd trigger a WhatsApp API call here
        send_whatsapp_alert(amount)
        
        return jsonify({"status": "success"}), 200

    return jsonify({"status": "failed"}), 400

def send_whatsapp_alert(amount):
    """
    This function connects to a WhatsApp API (like Twilio or Meta)
    to send you the automated 'Good received' message.
    """
    # Replace this URL with your chosen WhatsApp API provider
    print(f"Sending WhatsApp notification to {MY_NUMBER} for D{amount}...")

if __name__ == '__main__':
    # Runs the server on your Ubuntu 24.04
    app.run(host='0.0.0.0', port=5000, debug=True)
