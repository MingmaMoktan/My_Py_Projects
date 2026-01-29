"""
Here I have created the simple news app that you can use. 

Please use your own news api key. If you don't have the news api key you can create one by going to this url https://newsapi.org/

After creating the newsAPI key you can paste your API key in the key variable below 'key = "" '. And then run the app to see the news. Right now this only shows the url and title but to read the whole description you can click on the url to go to the particular news page. 
"""
import requests

query = input("Enter the topic you want to see news about: ")

date = input("Enter the date in format \'mm-dd\': ")

key = ""


url = f"https://newsapi.org/v2/everything?q={query}&from=2025-{date}&sortBy=publishedAt&apiKey={key}"

print(url)

r = requests.get(url)

news_data = r.json()

articles = news_data["articles"]

for article in articles:
    print(article["title"], article["url"])
    print("\n\n\n\n")