from sys import flags
from aiohttp import ClientSession
from urllib.parse import quote_plus


OVERPASS_API_INTERPRETER = "https://maps.mail.ru/osm/tools/overpass/api/interpreter"


async def query_osm(
    query: str, bbox: tuple[float, float, float, float] | None = None
) -> list:
    if "{{bbox}}" in query:
        if not bbox:
            raise ValueError("{{bbox}} in query, but it wasn't provided")
        p1, p2 = bbox[:2], bbox[2:]
        bottom_left = (min(p1[0], p2[0]), min(p1[1], p2[1]))
        top_right = (max(p1[0], p2[0]), max(p1[1], p2[1]))
        print(bbox, (*bottom_left, *top_right))
        query = query.replace(
            "{{bbox}}", ", ".join(map(str, (*bottom_left, *top_right)))
        )
    print(query)
    async with ClientSession() as session:
        async with session.post(
            OVERPASS_API_INTERPRETER, data="data=" + quote_plus("[out:json];" + query)
        ) as response:
            if response.content_type == "text/html":
                print(await response.text())
            return (await response.json())["elements"]


async def find_path(start: tuple[float, float], end: tuple[float, float]):
    return await query_osm(
        """
        way
            [railway=rail]
            [usage=main]
            ({{bbox}});
        out geom;
        """,
        (*start, *end),
    )
