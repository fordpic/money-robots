import aiohttp
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()
COINALYZE = os.getenv('COINALYZE_KEY')

# Query Params
symbols = """
BTCUSDT.P,
ETHUSDT.P,
MATICUSDT.P,
ARBUSDT.P,
FTMUSDT.P,
SOLUSDT.P,
LTCUSDT.P,
DOGEUSDT.P,
ATOMUSDT.P,
LINKUSDT.P,
AVAXUSDT.P,
DYDXUSDT.P,
BNBUSDT.P,
XRPUSDT.P
"""

endpoint = 'https://api.coinalyze.net/v1/open-interest'
