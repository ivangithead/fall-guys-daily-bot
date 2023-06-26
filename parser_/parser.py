import cfscrape
from data import URL

scraper = cfscrape.create_scraper()


def get_content(url: str) -> str:
    return scraper.get(url).json()["data"]["data"]


def get_current_shop() -> dict:
    content = get_content(URL)
    data = dict()

    for slot in content:
        for item in slot["items"]:
            if item["image_url_override"]:
                data[item["display_name"]] = {
                    "image": item["image_url_override"],
                    "price": item["payment"]["price"]
                }
    return data
