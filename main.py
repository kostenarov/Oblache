import psutil
import time

# Define the PID of the app's process
APP_PROCESS_PID = 17692

# Define the time interval between each CPU usage check (in seconds)
CPU_CHECK_INTERVAL = 5


def monitor_app_cpu_usage():
    while True:
        # Get the CPU usage of the app's process as a percentage
        app_cpu_percent = psutil.Process(APP_PROCESS_PID).cpu_percent()
        app_name = 
        # Print the app's CPU usage percentage
        print(f'App CPU usage: {app_cpu_percent}%')

        # Wait for the specified time interval before checking the CPU usage again
        time.sleep(CPU_CHECK_INTERVAL)

monitor_app_cpu_usage()