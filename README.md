# Caching Proxy Server

[Español](README.es.md) | English

A robust and modular Python solution to implement a **Proxy Server with a Persistent Caching Mechanism**. This project intercepts HTTP requests directed to an origin server, stores successful responses locally to optimize load times, and exposes a command-line interface (CLI) for administration.

Project developed following the specifications of the [roadmap.sh/projects/caching-server](https://roadmap.sh/projects/caching-server) challenge.

---

## Features

* **Full Transparent Proxy:** Capability to dynamically redirect any route, HTTP method, and query parameters to the origin server securely.
* **Efficient Static Resource Handling:** Robust configuration to capture and seamlessly serve CSS styles, JavaScript, images, and fonts without interfering with internal routes.
* **Persistent JSON-Based Cache:** Local storage that survives server restarts. Uses SHA-256 hashing of requests to generate unique filenames and **Base64** encoding to safely store binary content.
* **Network Diagnostic Headers:** Automatic insertion of the `X-Cache: HIT` header (if the resource was served from local storage) or `X-Cache: MISS` (if the origin server was queried).
* **Modular Architecture:** Strict separation of concerns between the entry point/CLI (`main.py`) and the web server logic (`server.py`).

---

## Prerequisites

* Python 3.8 or higher
* Configured and installed virtual environment (`venv`)

---

## Installation and Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Aki-new/proxy-cache.git]
   cd proxy-cache
2. **Activate the virtual environment and install dependencies:**
    ```bash
        # On Windows:
        .venv\Scripts\activate
        
        # On macOS/Linux:
        source .venv/bin/activate
        
        # Install required dependencies (Flask and Requests)
        pip install -r requirements.txt

## Usage Instructions
The project is managed entirely through the command-line interface (CLI) from the main.py file.

1. **Start the Proxy Server:**
    To start the proxy, the origin server URL must be specified. Optionally, a port can be provided (defaults to 5000):
    ```bash
    python main.py --port 3000 --origin https://www.python.org

2. **Verify Cache Functionality:**
Once the server is running, open a browser or use tools like curl or Postman to interact with it:

    * Initial Request (MISS): Accessing http://localhost:3000/ will download the content from the origin, create the local JSON file in the .cache/ folder, and respond by including the X-Cache: MISS header.

    * Subsequent Requests (HIT): Reloading the page or requesting the same resource will result in an instant response using the local file, including the X-Cache: HIT header.

3. **Clear Persistent Cache:**
To completely empty the local storage and delete the .cache/ folder, execute the command with the `--clear-cache flag`:

``` bash
python main.py --clear-cache