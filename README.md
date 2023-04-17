# Infrastructure Monitoring

This project implements an application to monitor infrastructure based on specified parameters. It includes a server and client code written in Python that communicates over a TCP/IP socket connection. The server collects and sends usage information (CPU usage, memory usage) of a specified application running on the server, while the client receives and visualizes the usage data in real-time using matplotlib.

## Architecture

The project consists of the following components:

- `server.py`: The server-side code that collects and sends usage information of the specified application running on the server. It uses the `psutil` library to monitor CPU usage, memory usage, and process information.

- `client.py`: The client-side code that receives the usage information from the server and visualizes the data in real-time using matplotlib. It also sends the name of the application to monitor to the server.

- `Dockerfile`: The Dockerfile for building a Docker image of the project. It uses the official Python 3.9 slim-buster base image and installs the required dependencies listed in `requirements.txt`.

- `requirements.txt`: The requirements file that lists the dependencies required by the project, including `psutil`, `matplotlib`, and `numpy`.

## Installation

To run the infrastructure monitoring project, follow these steps:

1. Clone the repository to your local machine:
```
git clone <repository-url>
```

2. Change to the project directory:
```
cd infrastructure-monitoring
```

3. Build the Docker image:
```
docker build -t infrastructure-monitoring .
```

4. Run the Docker container:
```
docker run -it --rm -p 12345:12345 infrastructure-monitoring
```

5. Open a new terminal window and run the client:
```
python3 client.py
```


6. Enter the name of the application you want to monitor when prompted by the client.

The client will start receiving usage information from the server and visualizing the data in real-time using matplotlib.

## Usage

- The `server.py` script should be run on the server where the application to monitor is running.

- The `client.py` script should be run on the client machine where you want to visualize the usage data.

- The `client.py` script will prompt you to enter the name of the application you want to monitor. Make sure to enter the correct name as it appears in the list of processes printed by the script.

- The client will continuously receive usage information from the server and update the plots in real-time. You can stop the monitoring by pressing Ctrl+C in the client terminal.
