#!Importing all libraries
from flask import Flask, render_template, request, jsonify
import os
import requests
from dotenv import load_dotenv

#!Loading all the environment variables
load_dotenv()

app = Flask(__name__)

#!Routing directly to the index.html file
@app.route("/home")
def index():
    return render_template("index.html")

#!Routing to the chat API method
@app.route("/api/chat", methods=["POST"])
def chat():
    #!Getting the user message from the request
    user_message = request.json.get("message")
    #!General Error Handling
    if not user_message:
        return jsonify({"reply": "Please provide a message."}), 400

    #!Headers and payload for the OpenRouter API (make sure to replace the API key with your own)
    #/Make it private
    headers = {
        "Authorization": f"Bearer",
        "Content-Type": "application/json"
    }
    #!Payload for the OpenRouter API
    #!Make sure to replace the model with the one you want to use
    #!Payload == Fancy way to say data
    payload = {
        "model": "google/gemma-3-1b-it:free",  # Updated model ID
        "messages": [
            {"role": "system", "content": "You are a calm and empathetic AI therapist helping users, speak in English and make your responses very short and make sure that you are understanding their situation, take some time to think about your response, make your responses to be shorter in length like a casual chat."},
            {"role": "user", "content": user_message}
        ]
    }

    #!Calling the OpenRouter API
    #!General Error Handling once again
    try:
        response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload)

        if response.status_code != 200:
            return jsonify({"reply": f"API error: {response.status_code} - {response.text}"}), 500

        response_data = response.json()

        if "choices" not in response_data or not response_data["choices"]:
            return jsonify({"reply": "The AI did not return any choices. Please try again."}), 500

        reply = response_data["choices"][0]["message"]["content"]
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"reply": f"Error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)

#!This was just a general check because I had some issues when I was doing the API calls before
#!I added this to check if it was working or not and decided to keep it as general error handling
#!Once again, this is not the best way to do it but it works for now