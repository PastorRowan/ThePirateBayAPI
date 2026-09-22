
import urllib.request
from pprint import pprint
import json

def main():

    RESPONSE_FILE_NAME: str = "response.json"

    QUERY: str = "ubuntu"

    URL: str = (
        "https://apibay.org/q.php?"
        + urllib.parse.urlencode({"q": QUERY})
    )

    HEADERS: dict[str, str] = {
        "Accept": "application/json",
        "User-Agent": "Mozilla/5.0"
    }

    REQUEST: urllib.request.Request = urllib.request.Request(
        url=URL,
        headers=HEADERS
    )

    print()
    print(f"Requesting '{URL}' with headers:")
    pprint(HEADERS)
    print()

    with urllib.request.urlopen(
        url=REQUEST
    ) as response:

        print("Parsing json response")
        print()

        # Type depends on what response is
        data: any = json.load(
            fp=response
        )

        print(f"Dumping pretty json response into '{RESPONSE_FILE_NAME}'")
        print()

        with open(
            file=RESPONSE_FILE_NAME,
            mode="w"
        ) as response_json_file:
            json.dump(
                obj=data,
                fp=response_json_file,
                indent=4
            )

    print(f"Successfully made request '{URL}' and dumped response into '{RESPONSE_FILE_NAME}'")

if __name__ == "__main__":
    main()
