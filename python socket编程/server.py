from chapter09.custom_socket import CustomSocket
from chapter09.socket_constant import SERVER_ADDRESS
import threading
if __name__ == '__main__':
    server = CustomSocket("服务器")
    server.sock.bind(SERVER_ADDRESS)
    server.sock.listen()

    def handle_sock(sender_sock, sender_address):
        data = sender_sock.receive_msg(sender_address, buffer=1)
        host, port = sender_address
        sender_sock.send_msg(f"已收到来自{host}:{port}的信息", sender_address)

    while True:
        sender, address = server.accept()
        thread = threading.Thread(target=handle_sock, args=(sender, address))
        thread.start()


    # while True:
    # thread = threading.Thread(target=)


