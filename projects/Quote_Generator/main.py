import requests

url = "https://official-joke-api.appspot.com/random_joke"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    print("=" * 50)
    print("😂 Random Joke")
    print("=" * 50)
    print()
    print(data["setup"])
    input("\nPress Enter for the punchline...")
    print()
    print(data["punchline"])
    print("=" * 50)

else:
    print(f"Failed to fetch joke. Status Code: {response.status_code}")