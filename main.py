import asyncio
from discord_bot import run_discord_bot

async def main():
    await run_discord_bot(),

if __name__ == "__main__":
    asyncio.run(main())