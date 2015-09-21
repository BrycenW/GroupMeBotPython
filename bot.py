#Brycen Wershing
from flask import Flask
import requests
import os

app = Flask(__name__)
@app.route('/')
def hello():
	return 'hello'

if __name__ == '__main__':
	port = int(os.environ.get("PORT",5000))
	app.run(host='0.0.0.0', port=port)

payload = {"text":"hello", "bot_id":"7e819111ff8f330b299db0679f"}
r = requests.post("https://api.groupme.com/v3/bots/post", params=payload)

