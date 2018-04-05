import socket
import datetime

def main():
    sock = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM,
        socket.IPPROTO_TCP)

    address = ('127.0.0.1', 3000)

    sock.bind(address)

    sock.listen(1)

    print(f'--- Starting server on port 3000 at {datetime.datetime.today()} ---')

    try:
        conn, addr = sock.accept()

        while True:
            data = conn.recv(2048)
            decoded = data.decode('utf8')
            if not data:
                break
            conn.sendall(data)
            print(f"[{datetime.datetime.today()}] echoed: {decoded}")

        print(f'--- Stopping server on port 3000 at {datetime.datetime.today()} ---')

        conn.close()
    except KeyboardInterrupt:
            conn.close()
            print('\n Ok, bye!')


if __name__ == "__main__":
    main()
