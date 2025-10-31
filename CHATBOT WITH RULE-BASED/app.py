from flask import Flask, render_template, request, jsonify
import random
from datetime import datetime

app = Flask(__name__)

# Rule-based chatbot logic
def chatbot_response(user_input):
    user = user_input.lower()

    # Greetings
    if any(word in user for word in ["hi", "hello", "hey"]):
        return random.choice(["Hello there! 👋", "Hey! How are you?", "Hi! What can I do for you?"])

    # Asking about time
    elif "time" in user:
        now = datetime.now().strftime("%I:%M %p")
        return random.choice([f"The current time is {now}. ⏰", f"It’s {now}, time flies fast!"])

    # Asking about date/day
    elif "date" in user or "day" in user:
        today = datetime.now().strftime("%A, %d %B %Y")
        return random.choice([f"Today is {today}. 📅", f"It’s a lovely {today}!"])

    # Asking name
    elif "your name" in user:
        return random.choice(["I’m SmartBot, created by Shibnath! 😎", "People call me SmartBot 🤖"])

    # Asking about AI or ChatGPT
    elif "ai" in user or "chatgpt" in user:
        return random.choice([
            "AI means Artificial Intelligence — smart machines like me! 🤖",
            "ChatGPT is my big brother, much smarter than me! 😅"
        ])

    # Asking for a joke
    elif "joke" in user:
        jokes = [
            "Why did the computer show up late? It had a hard drive! 😂",
            "Why was the computer cold? It left its Windows open! ❄️"
        ]
        return random.choice(jokes)

    # Bye
    elif "bye" in user or "exit" in user:
        return random.choice(["Goodbye! 👋", "See you soon!", "Bye-bye! Take care!"])

    # Unknown
    else:
        return random.choice([
            "Hmm... I’m not sure about that 🤔",
            "Interesting! Tell me more!",
            "Sorry, I don’t understand yet 😅"
        ])

# Flask routes
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["GET"])
def get_bot_response():
    user_text = request.args.get('msg')
    return chatbot_response(user_text)

if __name__ == "__main__":
    app.run(debug=True)
