from flask import Flask, send_file

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    # Serve the main page
    return send_file("index.html")

@app.route("/<path:path>", methods=["GET"])
def serve_static(path):
    # If additional static files are added later (like CSS or JS), serve them
    return send_file(path)

if __name__ == "__main__":
    # Local testing
    app.run( debug=True)
