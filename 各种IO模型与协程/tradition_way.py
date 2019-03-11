import socket
from urllib.parse import urlparse

class SocketHttp:
    """
    传统方式获取网页HTML内容（阻塞同步）
    """
    def __init__(self, url):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.url = url
        self._url = urlparse(self.url)
        self.host = self._url.netloc
        self.path = self._url.path
        if self.path == "":
            self.path = "/"

    def connect(self):
        self.client.connect((self.host, 80))

    def get_html(self):
        self.client.send(
            f"GET {self.path} HTTP/1.1\r\nHost:{self.host}\r\nConnection:close\r\n\r\n".encode(encoding='utf8'))
        data = b''

        while True:
            temp = self.client.recv(256)
            if temp:
                data += temp
            else:
                break
        return data.decode(encoding='utf8').split('\r\n\r\n')[1]


if __name__ == '__main__':
    import time

    start = time.time()
    html_list = []

    for i in range(20):
        url = "http://shop.projectsedu.com/goods/{}/".format(i)
        http_socket = SocketHttp(url)
        http_socket.connect()
        html_list.append(http_socket.get_html())
    end = time.time()
    cost = end - start
    print(f"总耗时：{cost}")
