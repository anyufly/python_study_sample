from chapter09.custom_socket import CustomSocket
from chapter09.socket_constant import SERVER_ADDRESS
import uuid

if __name__ == '__main__':
    client = CustomSocket("客户端_" + str(uuid.uuid1()))
    client.sock.connect(SERVER_ADDRESS)
    while True:
        msg = input()
        client.send_msg(msg, SERVER_ADDRESS)
        data = client.receive_msg(SERVER_ADDRESS, buffer=1)
