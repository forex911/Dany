import urllib.request
import json

def process_media(url):
    """
    Example script demonstrating how to interact with the Dany Template API
    using only standard Python libraries.
    """
    
    api_endpoint = "http://127.0.0.1:5000/process"
    
    # Prepare payload
    payload = {
        "url": url,
        "format": "mp3"
    }
    
    # Encode payload to bytes
    data = json.dumps(payload).encode('utf-8')
    
    # Set up request headers
    req = urllib.request.Request(
        api_endpoint, 
        data=data, 
        headers={'Content-Type': 'application/json'}
    )
    
    print(f"Sending request to {api_endpoint} for URL: {url}...")
    
    try:
        with urllib.request.urlopen(req) as response:
            status = response.status
            body = response.read().decode('utf-8')
            
            print(f"Status: {status}")
            print("Response:")
            print(json.dumps(json.loads(body), indent=2))
            
    except urllib.error.HTTPError as e:
        print(f"HTTP Error: {e.code} - {e.reason}")
        body = e.read().decode('utf-8')
        print(json.dumps(json.loads(body), indent=2))
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_url = "https://example.com/media/test_123"
    process_media(test_url)
