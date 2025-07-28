import socket

# import signal
# import sys


HOST = ''
PORT = 80 # if no IP forwarding else 5000


# def termination(signum, frame):
#     print("\n[INFO] Process terminated.")
#     sys.exit(0)


def check_port(h, p):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((h, p))
        s.listen()
        print(f"[INFO] Listening {p}... Waiting for incoming connection.")
        conn, addr = s.accept()
        with conn:
            print(f"[INFO] Got connection from: {addr}")
            data = conn.recv(1024)
            print(f"[INFO] Received data:\n{data.decode(errors='ignore')}")


if __name__ == "__main__":
    # signal.signal(signal.SIGINT, termination)
    check_port(HOST, PORT)