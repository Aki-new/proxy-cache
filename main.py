import argparse

if __name__ == "__main__":

    # Description
    parser = argparse.ArgumentParser(
        description="Caching Server"
    )

    # Port
    parser.add_argument(
        "--port", type=int, default=5000, help="Port where the proxy will run"
    )

    # URL
    parser.add_argument(
        "--origin",
        type=str,
        required=True,
        help="Origin server URL (ej. https://getcomposer.org)",
    )

    args = parser.parse_args()

    ORIGIN_URL = args.origin # Global variable

    print(f"Starting Proxy for: {ORIGIN_URL}")
    print(f"Listening in port: {args.port}")