import asyncio
import logging
import time
from collections import OrderedDict

logger_format = '%(asctime)s:%(threadName)s:%(message)s'
logging.basicConfig(format=logger_format, level=logging.INFO, datefmt="%H:%M:%S")


class DbUpdate:
    def __init__(self):
        self.value = 0

    async def update(self):
        logging.info("Update Started")
        logging.info("Sleeping")
        await asyncio.sleep(5)
        logging.info("Reading Value From Db")
        tmp = self.value ** 2 + 1
        logging.info("Updating Value")
        self.value = tmp
        logging.info("Update Finished")


async def main():
    db = DbUpdate()
    await asyncio.gather(*[db.update() for _ in range(2)])
    # show_coro(asyncio.all_tasks())
    logging.info(f"Final value is {db.value}")


def show_coro(c):
    data = OrderedDict([
        ('txt', str(c)),
        ('type', str(type(c))),
        ('done', c.done()),
        ('cancelled', False),
        ('stack', None),
        ('exception', None),
    ])
    if not c.done():
        data['stack'] = [format_frame(x) for x in c.get_stack()]
    else:
        if c.cancelled():
            data['cancelled'] = True
        else:
            data['exception'] = str(c.exception())
    return data


def format_frame(f):
    keys = ['f_code', 'f_lineno']
    return OrderedDict([(k, str(getattr(f, k))) for k in keys])


if __name__ == '__main__':
    asyncio.run(main())

