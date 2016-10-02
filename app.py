	# Copyright (c) 2016 Yaoxian Qu & Xuanrui Qi
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
# 
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
import requests
from flask import Flask, json, jsonify, request, render_template
from firebase import Firebase
from firebase_token_generator import create_token
from crossdomain import crossdomain

__author__ = 'Xuanrui Qi & Yaoxian Qu'

app = Flask(__name__)

base_url = "https://personality-recommender-80814.firebaseio.com/"
users_url = base_url + 'users'

auth_payload = {"uid": "lfeqCjaPdHdML4Jtgri23RFVzBm1"}
secret_key = "1G8cEGmnVLb20kWnpkmac3cSvEy1NZKJu0BJ0pRR"
options = {
	"debug": True,
	"admin": True
}

token = create_token(secret_key, auth_payload, options)
ref = Firebase(base_url, auth_token = token)
users_ref = Firebase(users_url, auth_token = token)

@app.route('/')
def hello():
    return jsonify(body="Hello, world!")


@app.route('/users/<username>', methods = ['GET'])
@crossdomain(origin='*')
def getPersonality(username):
	tweets = request.args.get("usertweet")
	tweets = json.loads(tweets)
	#calculate personality using request.data
	content = {"contentItems" : tweets}
	content = json.dumps(content)
	# print tweets
	try:
		personality = requests.post("https://gateway.watsonplatform.net/personality-insights/api/v2/profile", headers = {"Content-Type": "application/json"}, data = content, auth = ("9ee0234a-22c9-4144-87f9-a8b633bfc64c", "kDr5XgKT8mGh"))
	except Exception as e:
		print e
	else:
		print "no error here"

	# personality = json.loads(personality)
	personality = json.loads(personality.text)
	#update personality using username

	users_ref.patch({username: personality});


	# #calculate recommendation with k-means

	return "laji"

if __name__ == '__main__':
    app.run()