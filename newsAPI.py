from urllib.request import urlopen
import json
import requests

# Purpose:
#   - Read the API
#   - Parse through it
#   - Output contents onto a file
#   - When you read the description of the articles that is where you find the keyword

title_list, url_list, description_list = ([] for i in range(3))

user = input("Enter a keyword: ")

# Tesla URL
Tesla = 'https://newsapi.org/v2/everything?q=tesla&from=2021-11-26&sortBy=publishedAt&apiKey=0ad4ba45105840df8b002903c58a1c09'
# Apple URL
Apple = 'https://newsapi.org/v2/everything?q=apple&from=2021-12-25&to=2021-12-25&sortBy=popularity&apiKey=0ad4ba45105840df8b002903c58a1c09'
# Business headlines URL
Business = 'https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=0ad4ba45105840df8b002903c58a1c09'
# Techcrunch URL
TechCrunch = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=0ad4ba45105840df8b002903c58a1c09"
# WSJ URL
WSJ = "https://newsapi.org/v2/everything?domains=wsj.com&apiKey=0ad4ba45105840df8b002903c58a1c09"

urls = [Tesla, Apple, Business, TechCrunch, WSJ]

for j in range(len(urls)):
    data = json.load(urlopen(urls[j]))
    for i in data['articles']:
        # key value pairs in articles are stored in these variables
        titles = i['title']
        des = i['description']
        url = i['url']
        # if statement is true when keyword is present in article
        if user.lower() in des.lower():
            title_list.append(titles)
            url_list.append(url)
            description_list.append(des)

file = open(user+".txt", "w")
file.write("Keyword: " + user + '\n')

for i in range(len(title_list)):
    file.write('\n' + "Title: " + title_list[i])
    print("Description: " + description_list[i])
    file.write('\n' + "URL: " + url_list[i] + '\n')

# for i in range(len(title_list)):
#     print('\n' + "Title: " + title_list[i])
#     # print("Description: " + description_list[i])
#     print('\n' + "URL: " + url_list[i] + '\n')

print("Done")
file.close()