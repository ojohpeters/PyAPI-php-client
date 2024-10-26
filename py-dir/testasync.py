import time
import asyncio

async def timer():
    print("Starting main engine.....")
    await asyncio.sleep(1)
    print("Ending engine...")
    await asyncio.sleep(0.4)
    print("Clashed")

i  = 1    

async def printer():
    print()
async def main():
    await asyncio.gather(tastimerk(), printer())
asyncio.run(main())     