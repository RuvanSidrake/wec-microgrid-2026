import socket
import json

HOST = "localhost"
PORT = 8800

def solve_hour(state):
    buildings = []

    for b in state["loads"]:
        buildings.append({
            "solar": 0,
            "battery": 0,
            "grid": b["load"]
        })

    return {
        "buildings": buildings,
        "generator": 0
    }

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
            response = solve_hour(state)

            s.sendall((json.dumps(response) + "\n").encode("utf-8"))
            print("Sent response for hour.")


if __name__ == "__main__":
    main()