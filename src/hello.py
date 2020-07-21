from flask import Flask


app = Flask(__name__)

# app.secret_key = 'replace later'

@app.route("/", methods=['GET', 'POST'])
def hello():
    return "Stef Griffin"

if __name__ == '__main__':
    app.run()

