import requests
import time

while True:
    # Replace 'http://fastapi:8000' with the actual host name of the FastAPI container
    response = requests.get("http://robot_control:8888/")
    print(response.json())
    time.sleep(5)  # Adjust as needed
