from flask import Flask, request

app = Flask(__name__)

count = 0

@app.route('/', methods=['GET', 'POST'])
def index():
    global count
    if request.method == 'POST':
        count += 1 
        return '200 OK'
    else:
        message = f"<h1>You sent {count} requests</h1>"
        return message
    return 'OK'
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8000', debug=True)

