from requests import get


class AdditionalBlock:
    def __init__(self, search_string: str) -> None:
        self.url = "https://api.duckduckgo.com/"
        self.format = "json"
        self.search_string = search_string

    def get_json(self) -> dict or None:
        response = get(url=self.url, params={
            "q": self.search_string, "format": self.format
        }, headers={
            "Cookie": "ad=en_US"
        })
        if response.status_code >= 200 < 300:
            return response.json()

    def get(self) -> dict or None:
        data = self.get_json()
        if data and data["RelatedTopics"] and \
                data["Heading"] and data["AbstractText"]:

            data["Image"] = "https://duckduckgo.com" + data["Image"]
            if not data["Entity"]: data["Entity"] = "Unknown"
            else: data["Entity"] = str(data["Entity"]).capitalize()

            return data
