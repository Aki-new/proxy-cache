import argparse
import os
import shutil
import sys
from server import start_server

def main():
    parser = argparse.ArgumentParser(description="CLI para el Servidor Proxy Caché.")
    
    # Clear cache option
    parser.add_argument(
        "--clear-cache", 
        action="store_true", 
        help="Delete all cache store"
    )

    # Port
    parser.add_argument("--port", type=int, default=5000)
    # URL
    parser.add_argument("--origin", type=str, required="--clear-cache" not in sys.argv)

    args = parser.parse_args()

    if args.clear_cache:
        if os.path.exists(".cache"):
            shutil.rmtree(".cache")
            print("Cache cleared")
        else:
            print("Cache is empty")
        return  

    start_server(origin_url=args.origin, port_input=args.port)

if __name__ == "__main__":
    main()