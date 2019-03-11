import socket, threading
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 8008))
server.listen()


def handle_sock(sock, address):
    print("客户端{}:{}连接".format(address[0], address[1]))
    while True:
        data = ''
        while True:
            temp = sock.recv(1)
            if not temp:
                break
            data += temp.decode("utf8")

        print("收到{}:{}的信息：{}".format(address[0], address[1], data))
        re_data = input()
        print("发送信息给{}:{}".format(address[0], address[1]))
        sock.sendto(re_data.encode("utf8"), address)


while True:
    client_socket, client_address = server.accept()
    client_thread = threading.Thread(target=handle_sock, args=(client_socket, client_address))
    client_thread.start()

