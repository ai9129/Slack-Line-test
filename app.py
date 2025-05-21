from flask import Flask, request

app = Flask(__name__)

@app.route('/callback', methods=['POST'])
def callback():
    body = request.json
    print(body)  # userIdなどがここに含まれます
    return 'OK', 200

if __name__ == '__main__':
    app.run()