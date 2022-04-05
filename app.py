import os
import datetime

from flask import Flask, request, Response

from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True)

port = int(os.environ.get('PORT', 5000))


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/test', methods=['POST'])
def test():
    return "POST sent."


@app.route('/poland')
def poland():
    dt_now_pl = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=2)))
    return str(dt_now_pl)


@app.route('/mailrec', methods=["GET", "POST"])
def mailrec():
    req = request.get_data()
    # json_dict = json.load(str(req))
    print(req)
    print(type(req))
    # print(json_dict)
    return Response(status=200)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
