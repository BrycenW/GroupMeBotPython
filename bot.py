#Brycen Wershing
from flask import Flask
import requests

app = Flask(__name__)
@app.route('/')
def hello():
	return 'hello'

if __name__ == '__main__':
	app.run()

payload = {"text":"hello", "bot_id":"7e819111ff8f330b299db0679f"}
r = requests.post("https://api.groupme.com/v3/bots/post", params=payload)

