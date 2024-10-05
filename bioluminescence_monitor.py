
import random
import time

# Simulated bioluminescence monitoring
def monitor_bioluminescence():
    intensity_threshold = 50  # Arbitrary threshold for monitoring activity
    for i in range(10):
        bioluminescence_intensity = round(random.uniform(0, 100), 2)
        print(f"Bioluminescence Intensity: {bioluminescence_intensity}")
        
        # Check if intensity exceeds the threshold, indicating metabolic activity
        if bioluminescence_intensity > intensity_threshold:
            print(f"Alert: High bioluminescence detected! Intensity: {bioluminescence_intensity}")
        else:
            print("Normal bioluminescence levels.")
        
        time.sleep(2)

if __name__ == "__main__":
    print("Starting Bioluminescence Monitoring...")
    monitor_bioluminescence()
