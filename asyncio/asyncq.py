import asyncio
import random
import itertools as it
import os


async def makeitem(size: int = 5) -> str:
    return os.urandom(size).hex()


async def randsleep(a: int = 1, b: int = 5, caller=None) -> None:
    i = random.randint(0, 10)
    if caller:
        print(f"{caller} sleeping for {i} seconds.")
    await asyncio.sleep(i)


async def produce(name, q):
    n = random.randint(0, 2)
    print(f"Producing {n} items...")
    for _ in it.repeat(None, n):
        await randsleep(caller=f"Producer {name}")
        i = await makeitem()
        await q.put(i)
        print(f"Producer {name} added <{i}> to queue.")


async def consume(name, q: asyncio.Queue):
    while True:
        await randsleep(caller=f"Consumer {name}")
        i = await q.get()
        print(f"Comsumer {name} consuming item {i}")
        q.task_done() #Notifies task completed to return to 42 join()


async def main(nprod: int, ncons: int):
    q = asyncio.Queue()
    producers = [asyncio.create_task(produce(i, q)) for i in range(nprod)]
    consumers = [asyncio.create_task(consume(i, q)) for i in range(ncons)]

    await asyncio.gather(*producers)
    await q.join() #  Implicitly awaits consumers
    for c in consumers:
        print(f"Cancel --> {c.cancel()}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--nprod", type=int, default=1)
    parser.add_argument("-c", "--ncons", type=int, default=9)

    ns = parser.parse_args()
    asyncio.run(main(**ns.__dict__))


    
