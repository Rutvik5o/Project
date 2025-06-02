import requests


topic = str(input("Enter the topic that you want news:"))
api="b15f124572d04227a1e2ea5b2fff2700"

url = f"https://newsapi.org/v2/everything?q={topic}&from=2025-04-23&sortBy=publishedAt&apiKey={api}"


c= requests.get(url).json()

print("------")

d=c["articles"]

for index,artical in enumerate(d):
    print(f"Article\n {index+1}=>Title:{artical["title"]}\n")
    print(f"Description :{artical["description"]}\n")
    print(f"content:{artical["content"]}\n")
    print(f"Url:{artical["url"]}\n")
    print("------------------------------------------------------------")

    
    


