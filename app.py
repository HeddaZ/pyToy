from flask import Flask, abort, request, jsonify
import config

app = Flask(__name__)
if __name__ == '__main__':
    app.run()


@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello World!222222' + config.HOST
