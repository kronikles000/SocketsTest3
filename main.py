import socket
import threading as threading
import random as random
anonnum = random.randint(1,200000)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('8.8.8.8', 80))
localip = s.getsockname()[0]
print(localip) #prints ip
s.close

ip = input('Enter IP to connect to (not port) type "local" if your hosting: ')
if ip.lower() == 'local':
    ip = localip
    print('hosting locally')

while True:
    basicportq = input('Connect to main room? (y/n): ')
    if basicportq.lower() == 'y':
        port = 12345
        break
    elif basicportq.lower() == 'n':
        port = int(input('Type port number of alternative room (Number only): '))
        break
    else:
        print('try again')

print(f'Your username: Anon{anonnum}')

try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ip, port))

    print("Connected to server")
    def recieve():
        while True:
            messg = client.recv(1024).decode()
            print(messg)

    threading.Thread(target=recieve, daemon=True).start()
    def send():
        while True:
            tosend = str(input(''))
            client.sendall((f'Anon{anonnum}: {tosend}').encode())
    
    threading.Thread(target=send, daemon=True).start()
except:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', port))
    server.listen()

    print('socket server made')

    conn, addr = server.accept()
    #print(addr)
    def recieve():
        while True:
            messg = conn.recv(1024).decode()
            print(messg)


    threading.Thread(target=recieve, daemon=True).start()

    def send():
        while True:
            tosend = str(input(''))
            conn.sendall((f'Anon{anonnum}: {tosend}').encode())

    threading.Thread(target=send, daemon=True).start()

threading.Event().wait()

input('Program stopped')