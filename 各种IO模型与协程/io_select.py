from socket import AF_INET, SOCK_STREAM, socket
from urllib.parse import urlparse
from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE

urls = [f'http://www.jobbole.com/#{i}' for i in range(1, 21)]


class SocketHttp:

    _selector = DefaultSelector()
    _stop_flag = False

    def __init__(self, url):
        self._url = url
        parse = urlparse(url)
        self.host = parse.netloc
        self.path = parse.path
        if self.path == '':
            self.path == '/'
        self.client = socket(AF_INET, SOCK_STREAM)
        self.client.setblocking(False)
        self.data = b''
        self.connect()

    def connect(self):

        try:
            self.client.connect((self.host, 80))
        except BlockingIOError:
            pass
        type(self)._selector.register(self.client.fileno(), EVENT_WRITE, self.send_request)

    def send_request(self, key):
        self.__class__._selector.unregister(key.fd)
        self.client.send(
            f"GET {self.path} HTTP/1.1\r\nHost:{self.host}\r\nConnection:close\r\n\r\n".encode(encoding='utf8'))
        type(self)._selector.register(self.client.fileno(), EVENT_READ, self.receive_response)

    def receive_response(self, key):
        temp = self.client.recv(1024)
        if temp:
            self.data += temp
        else:
            type(self)._selector.unregister(key.fd)
            self.client.close()
            urls.remove(self._url)
            self.data = self.data.decode(encoding='utf-8')
            print(self.data)
            print(f'load {self._url} over')
            if not urls:
                type(self)._stop_flag = True

    @classmethod
    def loop(cls):
        while not cls._stop_flag:
            ready = cls._selector.select()
            for key, mask in ready:
                callback = key.data
                callback(key)


if __name__ == '__main__':
    from datetime import datetime
    time1 = datetime.now()

    socket_https = [SocketHttp(url=url) for url in urls]

    SocketHttp.loop()
    time2 = datetime.now()

    print(time2 - time1)


