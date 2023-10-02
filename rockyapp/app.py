from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_geek():
    return '<marquee><big>Hello from Rocky World</big></marquee>'


if __name__ == "__main__":
    app.run(debug=True, port=9090, host='0.0.0.0')
