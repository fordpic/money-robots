import aiohttp
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()
COINALYZE = os.getenv('COINALYZE_KEY')

# Query Params
symbols = "BTCUSDT_PERP.0,ETHUSDT_PERP.0,MATICUSDT_PERP.0,FTMUSDT_PERP.0,SOLUSDT_PERP.0,ARBUSDT_PERP.0,"

async def fetch(client):
    async with client.get(f"https://api.coinalyze.net/v1/open-interest?symbols={symbols}&api_key={COINALYZE}") as res:
        assert res.status == 200
        return await res.json()


async def main():
    print("Grabbing OI data from Coinalyze...")

    async with aiohttp.ClientSession() as client:
        data = await fetch(client)

        result = []

        for key in data:
            for item in key.items():
                # print(item[1])
                result.append(item[1])


        print(result)
        return result

loop = asyncio.get_event_loop()
loop.run_until_complete(main())