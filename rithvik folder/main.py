from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Student Management System</h1>
    <h2>Application deployed successfully!</h2>
    """

if __name__ == "__main__":
    import os
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))