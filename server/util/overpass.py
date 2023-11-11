from aiohttp import ClientSession
from urllib.parse import quote_plus


OVERPASS_API_INTERPRETER = "https://maps.mail.ru/osm/tools/overpass/api/interpreter"


async def query_osm(query: str, bbox: tuple[int, int, int, int] | None = None) -> list:
    if "{{bbox}}" in query:
        if not bbox:
            raise ValueError("{{bbox}} in query, but it wasn't provided")
        query = query.replace("{{bbox}}", ", ".join(map(str, bbox)))

    async with ClientSession() as session:
        async with session.post(
            OVERPASS_API_INTERPRETER, data="data=" + quote_plus("[out:json];" + query)
        ) as response:
            return (await response.json())["elements"]


async def find_path(start: tuple[int, int], end: tuple[int, int]):
    await query_osm(
        f"""
        [out:json];
        way
            [railway=rail]
            [usage=main]
            ({{bbox}});
        out geom;
        """,
        (*start, *end),
    )
