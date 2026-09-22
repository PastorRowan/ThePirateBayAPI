
# ThePirateBayAPI

A small Python project for experimenting with making HTTP requests to [The Pirate Bay](https://thepiratebay.org/index.html) API using Python's built-in urllib.request.

The program:

- Sends a search request for a specified query.
- Requests the response as JSON.
- Parses the JSON response.
- Saves the response as a pretty-printed response.json file.

## Requirements

- [Python 3.13+](https://www.python.org/downloads/)
- **No external dependencies.**

## Usage

Run:
```
python main.py
```

The default query is:
```
ubuntu
```

The resulting JSON response is written to:
```
response.json
```

## Technologies

- [Python](https://www.python.org/)
- [urllib](https://docs.python.org/3/library/urllib.html)
- [pprint](https://docs.python.org/3/library/pprint.html)
- [json](https://docs.python.org/3/library/json.html)
