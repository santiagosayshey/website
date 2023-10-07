import json
import requests


# Define constants
base_url = "http://localhost:7878"
api_key = "API_KEY_GOES_HERE"

# Define parameters and headers
params = {"apikey": api_key}
headers = {"X-Api-Key": api_key}
files = {'file': ('', '')}  # Empty file to force multipart/form-data

# Login
login_url = f"{base_url}/login"
response = requests.get(login_url, params=params, headers=headers, files=files)

if response.status_code != 200:
    print(f"Login Failed! (HTTP {response.status_code})")
    print("Response Content: ", response.content)
    exit()


def get_and_save_custom_formats():
    custom_format_url = f"{base_url}/api/v3/customformat"
    response = requests.get(custom_format_url, params=params, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        
        # Remove 'id' from each custom format
        for custom_format in data:
            custom_format.pop('id', None)
        
        # Save to JSON file
        with open('custom_formats_dump.json', 'w') as f:
            json.dump(data, f, indent=4)
        print("Custom Formats have been saved to 'custom_formats_dump.json'")
    else:
        print(f"Failed to retrieve custom formats! (HTTP {response.status_code})")
        print("Response Content: ", response.content)


def post_custom_formats():
    # Load the data from the JSON file
    with open('custom_formats_dump.json', 'r') as f:
        custom_formats = json.load(f)
    
    for format in custom_formats:
        post_url = f"{base_url}/api/v3/customformat"
        
        # Send POST request
        response = requests.post(post_url, json=format, params=params, headers=headers)
        
        if response.status_code in [200, 201]:
            print(f"Successfully posted custom format {format['name']}! (HTTP {response.status_code})")
        else:
            print(f"Failed to post custom format {format['name']}! (HTTP {response.status_code})")
            print("Response Content: ", response.content)

if __name__ == "__main__":
    