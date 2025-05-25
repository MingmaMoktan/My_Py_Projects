import requests

query = input("Enter the topic you want to see news about: ")

date = input("Enter the date in format mm-dd: ")

key = "b3c286f32b2341978eb3ccb0501f0b38"


url = f"https://newsapi.org/v2/everything?q={query}&from=2025-{date}&sortBy=publishedAt&apiKey={key}"

print(url)

r = requests.get(url)

news_data = r.json()

articles = news_data["articles"]

for article in articles:
    print(article["title"], article["url"])
    print("\n\n\n\n")