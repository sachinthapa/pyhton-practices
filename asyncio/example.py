import random
import asyncio

c = (
    "\033[0m",   # End of color
    "\033[36m",  # Cyan
    "\033[91m",  # Red
    "\033[35m",  # Magenta
    )


async def makerandom(indx: int, threshold: int = 0) -> int:
    print(c[indx + 1] + f"Initiated make random {indx} threshold {threshold} ")

    i = random.randint(0, 10)
    print(c[indx +1] + f" i [{i}] ") 
    
    while i <= threshold:
        print(c[indx + 1] + f"making random {indx} == {i} retrying.... ")
        await asyncio.sleep(indx + 1)
        i = random.randint(0, 10)
        print(f"random  [{i} <= {threshold}]   " )
    print(c[indx + 1] + f"Finished making random {indx} == {i} " + c[0])
    return i


async def main():
    random.seed(444)

    res = await asyncio.gather(*(makerandom(i, 10 - i - 1) for i in range(2)))
    return res


if __name__ == "__main__":
    asyncio.run(main())
