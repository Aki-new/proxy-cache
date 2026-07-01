import os
import json
import base64
import hashlib

CACHE_DIR = ".cache"

def get_cache_filename(target_url, query_params):
    sorted_params = sorted(query_params.items()) if query_params else []
    
    unique_string = f"{target_url}_{sorted_params}"
    
    url_hash = hashlib.sha256(unique_string.encode('utf-8')).hexdigest()
    
    return os.path.join(CACHE_DIR, f"{url_hash}.json")

def save_to_cache(filepath, content_bytes, status_code, content_type):
    """Guarda la respuesta convirtiendo los bytes a texto en Base64."""
    os.makedirs(CACHE_DIR, exist_ok=True)
    
    encoded_content = base64.b64encode(content_bytes).decode('utf-8')
    
    cache_data = {
        "status": status_code,
        "content_type": content_type,
        "content": encoded_content
    }
    
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(cache_data, f, indent=4)

def load_from_cache(filepath):
    if not os.path.exists(filepath):
        return None
        
    with open(filepath, "r", encoding="utf-8") as f:
        cache_data = json.load(f)
        
    decoded_content = base64.b64decode(cache_data["content"].encode('utf-8'))
    
    return {
        "content": decoded_content,
        "status": cache_data["status"],
        "content_type": cache_data["content_type"]
    }