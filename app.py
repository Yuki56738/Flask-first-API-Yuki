import os

from flask import Flask

app = Flask(__name__)

port = int(os.environ.get('PORT', 5000))

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/test', methods=['POST'])
def test():
    return "POST sent."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
