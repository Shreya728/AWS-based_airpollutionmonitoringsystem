import random
import time
import requests

def generate_pollution_data():
    locations = ["City Center", "Industrial Area", "Residential Area", "Park", "Complex", "Airport", "School"]
    pm25 = round(random.uniform(10, 300), 2)
    pm10 = round(random.uniform(10, 400), 2)
    co2 = round(random.uniform(300, 1000), 2)
    location = random.choice(locations)
    region_id = f"region_{location.replace(' ', '_').lower()}"  # Generate region_id

    return {
        "location": location,
        "pm25": pm25,
        "pm10": pm10,
        "co2": co2,
        "timestamp": int(time.time()),  # Ensure timestamp is an integer
        "region_id": region_id
    }

def send_data_to_server(data):
    url = "http://13.48.46.96:8080/sensor-data"  # Update with your actual server IP
    try:
        response = requests.post(url, json=data)
        if response.status_code == 200:
            print(f"Data sent successfully: {data}")
        else:
            print(f"Failed to send data. Status Code: {response.status_code}, Response: {response.text}")
    except Exception as e:
        print(f"Error sending data: {str(e)}")

if __name__ == "__main__":
    while True:
        data = generate_pollution_data()
        send_data_to_server(data)
        time.sleep(40)
