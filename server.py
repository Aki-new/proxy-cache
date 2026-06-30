from flask import Flask, Response
import requests

app = Flask(__name__)
ORIGIN_URL = None

@app.route("/")
def health():
    return "<p>Server is running</p>"

@app.route("/page")
def page():
    if ORIGIN_URL is None:
        return "Origin URL not configured", 500

    page = requests.get(ORIGIN_URL)

    return Response(
        page.content,
        status=page.status_code,
        content_type=page.headers.get('Content-Type')
    )

if __name__ == "__main__":
    app.run(debug=True)

def start_server(origin_url: str, port_input: int = 5000):
    global ORIGIN_URL
    ORIGIN_URL = origin_url
    app.run(debug=True, port=port_input)