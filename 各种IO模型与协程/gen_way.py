import socket
from selectors import DefaultSelector, EVENT_WRITE, EVENT_READ
from urllib.parse import urlparse

selector = DefaultSelector()
result = {}
stop_flag = False


def get_send_data(client, path, host):
    yield
    selector.unregister(client.fileno())
    send_data = f"GET {path} HTTP/1.1\r\nHost:{host}\r\nConnection:close\r\n\r\n".encode(encoding='utf8')
    return send_data


def get_receive_data(client):
    data = b''
    while True:
        x = yield
        if not x:
            break
        temp = client.recv(1024)
        if temp:
            data += temp
        else:
            global stop_flag
            stop_flag = True
    return data


def downloader(url):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.setblocking(False)

    _url = urlparse(url)
    host = _url.netloc
    path = _url.path
    if path == "":
        path = "/"

    try:
        client.connect((host, 80))
    except BlockingIOError:
        pass

    selector.register(client.fileno(), EVENT_WRITE)
    send_data = yield from get_send_data(client, path, host)

    client.send(send_data)
    selector.register(client.fileno(), EVENT_READ)

    source = yield from get_receive_data(client)
    return source.decode(encoding='utf8').split('\r\n\r\n')[1]


def download_html(url):
    html = yield from downloader(url)
    result[url] = html
    yield
    return html


def loop(gen):
    gen.send(None)
    while not stop_flag:
        ready = selector.select()
        for key, mask in ready:
            gen.send('next')
    gen.send(None)


if __name__ == '__main__':
    url = 'https://www.baidu.com'
    gen = download_html(url)
    loop(gen)
    print(result)
