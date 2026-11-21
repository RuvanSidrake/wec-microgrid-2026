import socket
import json

HOST = "localhost"
PORT = 8800


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print(f"Connecting to {HOST}:{PORT}...")
        s.connect((HOST, PORT))
        print("Connected!")

        reader = s.makefile("r", encoding="utf-8")

        for line in reader:
            line = line.strip()
            if not line:
                continue

            state = json.loads(line)
            print("Received state:", state)


if __name__ == "__main__":
    main()