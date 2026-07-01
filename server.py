from flask import Flask, Response, request
import requests
from cache import get_cache_filename, load_from_cache, save_to_cache

app = Flask(__name__, static_folder=None)
ORIGIN_URL = None

@app.route("/proxy-status-health")
def health():
    return "<p>Server is running</p>"

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def proxy_global(path):
    if ORIGIN_URL is None:
        return "Origin URL not configured", 500

    base_origin = ORIGIN_URL.rstrip('/')
    target_path = path or ""
    target_url = f"{base_origin}/{target_path}" if target_path else base_origin

    query_params = request.args.to_dict()
    filepath = get_cache_filename(target_url, query_params)

    cached_response = load_from_cache(filepath)

    if cached_response:
        # ¡HIT!
        return Response(
            cached_response["content"],
            status=cached_response["status"],
            content_type=cached_response["content_type"],
            headers={"X-Cache": "HIT"}
        )

    try:
        headers = {}
        for key, value in request.headers.items():
            if key.lower() not in ['host', 'accept-encoding']: 
                headers[key] = value

        origin_response = requests.request(
            method=request.method,
            url=target_url,
            params=query_params,
            headers=headers,
            timeout=10,
            allow_redirects=True,
        )

        content_type = origin_response.headers.get("Content-Type") or "text/html; charset=utf-8"

        save_to_cache(filepath, origin_response.content, origin_response.status_code, content_type)
        
        return Response(
            origin_response.content,
            status=origin_response.status_code,
            content_type=content_type,
            headers={"X-Cache": "MISS"}
        )
        
    except requests.exceptions.RequestException as e:
        return f"Error al conectar con el origen: {str(e)}", 502

def start_server(origin_url: str, port_input: int = 5000):
    global ORIGIN_URL
    ORIGIN_URL = origin_url

    print(f"Starting proxy to: {ORIGIN_URL}")
    print(f"Running in http://localhost:{port_input}")
    app.run(debug=True, port=port_input, threaded=True)

if __name__ == "__main__":
    start_server("https://getcomposer.org", 5000)