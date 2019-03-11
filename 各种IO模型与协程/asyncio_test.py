import asyncio
import time
from functools import partial


async def get_html():
    print('start get html')
    await asyncio.sleep(2)
    print('end get html')
    return "123"


# 先执行callback在返回
def callback(param, futrue):
    print(f"callback {param}")


if __name__ == '__main__':
    start_time = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_html())

    tasks = [get_html() for i in range(10)]
    loop.run_until_complete(asyncio.wait(tasks))

    future = asyncio.ensure_future(get_html())
    loop.run_until_complete(future)

    task = loop.create_task(get_html())
    # 使用partial包装函数
    task.add_done_callback(partial(callback, 'partial test'))
    loop.run_until_complete(task)
    print(task.result())

    print(future.result())
    print(time.time() - start_time)
