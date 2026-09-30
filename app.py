from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! CI/CD Cloud Application is Running."

@app.route("/about")
def about():
    return "This application is deployed using CI/CD."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)