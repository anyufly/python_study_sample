import socket
from urllib.parse import urlparse


class SocketHttp:
    """
    使用非阻塞的方式获取页面数据
    """
    def __init__(self, url):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.setblocking(False)
        self.url = url
        self._url = urlparse(self.url)
        self.host = self._url.netloc
        self.path = self._url.path
        if self.path == "":
            self.path = "/"

    def connect(self):
        try:
            self.client.connect((self.host, 80))
        except BlockingIOError:
            pass

    def get_html(self):
        while True:
            try:
                self.client.send(
                    f"GET {self.path} HTTP/1.1\r\nHost:{self.host}\r\nConnection:close\r\n\r\n".encode(encoding='utf8'))
            except OSError:
                pass
            else:
                break
        data = b''

        while True:
            try:
                temp = self.client.recv(256)
            except BlockingIOError:
                continue

            if temp:
                data += temp
            else:
                break
        return data.decode(encoding='utf8').split('\r\n\r\n')[1]

    def process(self):
        self.connect()
        data = self.get_html()
        return data


if __name__ == '__main__':
    import time

    start = time.time()
    html_list = []

    for i in range(20):
        url = f'http://www.jobbole.com/#{i}'
        http_socket = SocketHttp(url)
        data = http_socket.process()
        html_list.append(data)
    end = time.time()
    cost = end - start
    print(f"总耗时：{cost}")
