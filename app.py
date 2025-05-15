from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template('index.html')

@app.route("/<path:path>", methods=["GET"])
def serve_static(path):
    # If additional static files are added later (like CSS or JS), serve them
    return send_file(path)

if __name__ == "__main__":
    # Local testing
    app.run( debug=True)
