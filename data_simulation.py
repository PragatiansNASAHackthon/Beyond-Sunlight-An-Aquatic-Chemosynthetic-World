
import random
import time

# Simulated environmental data collection (temperature, pH, salinity)
def collect_data():
    data = {
        'temperature': round(random.uniform(2, 10), 2),  # Deep-sea temperatures
        'ph': round(random.uniform(7.5, 8.5), 2),        # Ideal pH range
        'salinity': round(random.uniform(34, 37), 2),    # Salinity levels in PSU
        'bioluminescence_intensity': round(random.uniform(0, 100), 2)  # Mock bioluminescence data
    }
    return data

# Simulating continuous data collection
def simulate_data_collection():
    for i in range(10):
        data = collect_data()
        print(f"Data point {i+1}: {data}")
        time.sleep(1)

if __name__ == "__main__":
    print("Starting IoT Sensor Data Simulation...")
    simulate_data_collection()
