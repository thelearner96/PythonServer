import socket

def Main():
    host = '10.0.0.14'
    port = 7667

    s = socket.socket()
    s.bind((host, port))

    s.listen(1)
    c, addr = s.accept()

    print("Recieved Connection From: " + str(addr))

    while True:
        data = c.recv(1024)
        if not data:
            break
        print(str(addr) + ": " + str(data))
    c.close()
    s.close()

if __name__ == '__main__':
    Main()
