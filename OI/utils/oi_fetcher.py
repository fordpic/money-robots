import aiohttp
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()
COINALYZE = os.getenv('COINALYZE_KEY')

# Query Params
symbols = str('BTCUSDT')



async def main():

    async with aiohttp.ClientSession() as session:
        endpoint = f'https://api.coinalyze.net/v1/open-interest?symbols=BTCUSDT&api_key={COINALYZE}'

        async with session.get(endpoint) as res:
            tokens = await res.json()
            print(tokens)
            print(symbols)

asyncio.run(main())