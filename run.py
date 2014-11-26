from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<span style='color:red'>I am app 1</span>"

@app.route('/hello/')
def hello():
    return "hello flask and uwsgi"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)