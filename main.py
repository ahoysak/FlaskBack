from flask import Flask, request
import requests
import flask_jsonpify


app = Flask(__name__)


@app.route('/search', methods=['GET'])
def search():
    if request.method == 'GET':
        args = request.args

    topics = requests.get(f"https://api.github.com/search/topics?q={args['title']}").json()
    response = flask_jsonpify.jsonpify(topics['items'])
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


if __name__ == '__main__':
    app.run(debug=True)
