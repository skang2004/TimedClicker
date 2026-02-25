import keyboard
import pyautogui
from datetime import datetime
import time
import sys

pyautogui.PAUSE = 0

# Variables to store mouse position
mouse_x, mouse_y = None, None

# Variables to store user input
time_h, time_m, time_s = None, None, None

# Function to save mouse position
def save_mouse_position():
    global mouse_x, mouse_y
    mouse_x, mouse_y = pyautogui.position()
    print(f"Mouse position saved: X={mouse_x}, Y={mouse_y}")

# Function to input and save time
def input_time():
    global time_h, time_m, time_s
    try:
        time_h = int(input("Enter hours: "))
        time_m = int(input("Enter minutes: "))
        time_s = int(input("Enter seconds: "))
        print(f"Time saved: {time_h}:{time_m}:{time_s}")
    except ValueError:
        print("Invalid input. Please enter numeric values for time.")

# Function to continuously compare PC time and perform mouse click
def continuous_compare_and_click():
    global time_h, time_m, time_s, mouse_x, mouse_y
    if None in (time_h, time_m, time_s, mouse_x, mouse_y):
        print("Please ensure all inputs are provided and mouse position is saved.")
        return

    try:
        user_time = datetime.strptime(f"{time_h}:{time_m}:{time_s}", "%H:%M:%S")
        cmp_cnt = 0
        while True:
            current_time = datetime.now()
            remaining_time = user_time - current_time

            if current_time.time() > user_time.time():
                pyautogui.click(mouse_x, mouse_y, duration=0)
                print("Mouse clicked at saved position. Exiting program.")
                break

            cmp_cnt += 1
            interval = 0.005  # 1/200 second
            print_interval = int(1/interval)  # Print every 1 second
            if cmp_cnt % print_interval == 0:
                cmp_cnt = 0
                _, remainder = divmod(remaining_time.seconds, 3600)
                minutes, seconds = divmod(remainder, 60)
                print(f"Remaining time: {minutes} minutes, {seconds} seconds")

            time.sleep(interval)  # Sleep for 1/100 second
    except Exception as e:
        print(f"Error: {e}")

# Function to execute all steps sequentially
def execute_all():
    save_mouse_position()
    input_time()
    continuous_compare_and_click()

# Bind F10 key to execute all steps sequentially
keyboard.wait('F10')  # Wait for F10 key press to start the program
execute_all()  # Execute the main function after F10 is pressed