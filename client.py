import socket
import time
import psutil
import matplotlib.pyplot as plt


cpu_usage_values = []
memory_usage_values = []

plt.ion()
fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True)

ax1.set_ylabel("CPU Usage (%)")
ax1.set_ylim([0, 100])
line1, = ax1.plot([], [], '-')
ax2.set_ylabel("Memory Usage (%)")
ax2.set_ylim([0, 8000])
line2, = ax2.plot([], [], '-')

for proc in psutil.process_iter():
    try:
        process_name = proc.name()
        process_id = proc.pid
        print(f"Process Name: {process_name}, PID: {process_id}")
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass

app_name = input('Enter the name of the application: ')

while True:
    time.sleep(2)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))
    client_socket.sendall(app_name.encode('utf-8'))

    usage_info = client_socket.recv(1024).decode('utf-8')
    usage_info = usage_info.split(',')
    cpu_usage = float(usage_info[0])
    memory_usage = float(usage_info[1])
    print(f"CPU Usage: {cpu_usage} %, Memory Usage: {memory_usage} %")
    cpu_usage_values.append(cpu_usage)
    memory_usage_values.append(memory_usage)

    x_data = list(range(len(cpu_usage_values)))
    line1.set_data(x_data, cpu_usage_values)
    ax1.set_xlim([max(0, len(cpu_usage_values) - 10), len(cpu_usage_values)])
    line2.set_data(x_data, memory_usage_values)
    ax2.set_xlim([max(0, len(memory_usage_values) - 10), len(memory_usage_values)])
    fig.show()
    fig.canvas.draw()
    client_socket.close()
