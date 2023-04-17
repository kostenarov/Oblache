import socket
import threading
import psutil
from concurrent.futures import ThreadPoolExecutor

MAX_THREADS = 10


def getInfo(app_name):
    pid = None
    for process in psutil.process_iter(['name', 'pid']):
        if process.info['name'] == app_name:
            pid = process.info['pid']
            break

    if pid is not None:
        process = psutil.Process(pid)
        cpu_percent = process.cpu_percent(interval=1)
        memory_info = process.memory_info()
        rss = memory_info.rss / 1024 / 1024
        vms = memory_info.vms / 1024 / 1024
        usage = [cpu_percent, rss, vms]
        usage_info = f"{cpu_percent}, {rss:.2f}, {vms:.2f}"
        return usage_info
    else:
        return "Process not found"


def handle_client(client_socket, address):
    while True:
        app_name = client_socket.recv(1024).decode('utf-8')
        if not app_name:
            break

        usage_info = getInfo(app_name)
        client_socket.sendall(usage_info.encode('utf-8'))

    client_socket.close()


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen()

print("Server is running...")

thread_pool = ThreadPoolExecutor(max_workers=MAX_THREADS)

while True:
    client_socket, address = server_socket.accept()
    thread_pool.submit(handle_client, client_socket, address)
