import serial
import pyttsx3
import math
import time

engine = pyttsx3.init()
try:
    ser = serial.Serial('COM9', 115200, timeout=1) 
    print("Connected to Arduino!")
except:
    print("Error: Check USB cable or COM Port number!")
    exit()


dataset = {

    "Yes":        [700, 700, 700, 700, 700], # Clench your fists tightly (high value on all fingers).
    "No":         [600, 600, 600, 150, 150], # Spread your fingers (index and middle fingers extended).
    "OK":         [400, 450, 150, 150, 150], # Point with index finger and thumb to form a circle.
    "Peace":      [600, 150, 150, 600, 600], # Raise index and middle fingers.
    "Good Luck":  [150, 700, 700, 700, 700]  # Raise thumb (Thumbs Up)
}

THRESHOLD = 375
last_spoken = ""

def calculate_distance(v1, v2):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(v1, v2)))

print("--- Starting Sign Language Translation (System Ready) ---")

while True:
    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8', errors='ignore').strip()
        try:
         
            current_data = [int(x) for x in line.split(',')]
            if len(current_data) != 5: continue

            best_match = "None"
            min_dist = 999999

            for name, ref_data in dataset.items():
                dist = calculate_distance(current_data, ref_data)
                if dist < min_dist:
                    min_dist = dist
                    best_match = name

            if min_dist < THRESHOLD:
                if best_match != last_spoken:
                    print(f"Detected gesture: {best_match} (Accuracy: {int(min_dist)})")
                    ser.write(f"{best_match}\n".encode())
                    engine.say(best_match)
                    engine.runAndWait()
                    last_spoken = best_match
            else:
                if last_spoken != "None":
                    print("Status: Waiting for next gesture...")
                    last_spoken = "None"

        except Exception as e:
            continue