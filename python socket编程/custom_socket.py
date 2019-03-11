import socket


class CustomSocket:
    """
    自定义socket客户端
    """
    def __init__(self, name, sock=None):
        """
        客户端初始化
        :param sock: socket对象
        :return:
        """
        if sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock
        self.name = name

    def accept(self):
        sock, address = self.sock.accept()
        return self.__class__(None, sock=sock), address

    def send_msg(self, message, address):
        host, port = address
        message = message.encode("utf8")

        sent = self.sock.send(message)
        if sent == 0:
            raise RuntimeError("连接已关闭")
        print("发送信息给{}:{}".format(host, port))
        return sent

    def receive_msg(self, address, buffer=None):
        if buffer is None:
            buffer = 2048
        data = ""
        host, port = address

        while True:
            temp = self.sock.recv(buffer)
            if not temp:
                break
            data += temp.decode("utf8")
        print("收到{}:{}的信息：{}".format(host, port, data))
        return data


