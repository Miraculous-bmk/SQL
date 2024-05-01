import socket

def check_mysql_status():
    # Check if MySQL server is running
    try:
        # Create a socket connection to localhost on port 3306 with a timeout of 5 seconds
        s = socket.create_connection(("localhost", 3306), timeout=5)
        s.close()
        print("MySQL server is running and accepting connections.")
    except ConnectionRefusedError:
        print("MySQL server is not running or refusing connections.")
    except TimeoutError:
        print("Connection attempt to MySQL server timed out. Check network configuration.")
    except socket.gaierror as e:
        print(f"Error occurred while connecting to MySQL server: {e}. Check host and port.")
    except Exception as e:
        print(f"Error occurred while checking MySQL server status: {e}")

if __name__ == "__main__":
    check_mysql_status()
