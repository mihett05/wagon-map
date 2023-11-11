import asyncio
from init_server import init_db
from parser.coords import parse_coords_json
from parser.peregon import parse_peregon_to_json


async def main():
    await init_db()
    parse_coords_json()
    parse_peregon_to_json()


if __name__ == "__main__":
    asyncio.run(main())
