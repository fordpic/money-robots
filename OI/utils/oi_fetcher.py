import aiohttp
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()
COINALYZE = os.getenv('COINALYZE_KEY')

# Query Params
symbols = str('BTCUSDT')

async def fetch(client):
    async with client.get(f'https://api.coinalyze.net/v1/open-interest?symbols=BTCUSDT&api_key={COINALYZE}') as res:
        assert res.status == 200
        return await res.text()


async def main():

    async with aiohttp.ClientSession() as client:
        data = await fetch(client)
        print(data)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())