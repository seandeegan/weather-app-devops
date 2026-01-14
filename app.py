from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def get_weather():
    # In a real app, this would call an API. 
    # For our 'Boring App', we just return a static JSON.
    return jsonify({
        "status": "online",
        "city": "Athol",
        "temperature": "32F",
        "condition": "Cold (Perfect for Linux servers)"
    })

if __name__ == '__main__':
    # We use port 5000 by default
    app.run(host='0.0.0.0', port=5000)
