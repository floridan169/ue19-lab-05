import requests

def main():
    url = "https://official-joke-api.appspot.com/random_joke"

    response = requests.get(url)

    if response.status_code != 200:
        print("Erreur :", response.status_code)
        return

    data = response.json()

    print("\n😄 Blague :")
    print(data["setup"])
    print("➡️", data["punchline"])

if __name__ == "__main__":
    main()
