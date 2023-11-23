import bs4 
import requests

result = requests.get("https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/Kings_Cross_Platform_9%2C75.jpg/220px-Kings_Cross_Platform_9%2C75.jpg")

with open("harry_image.jpg", "wb") as f :
    f.write(result.content)

#briny content的抓取
# print(result)
# print(result.content)

# soup = bs4.BeautifulSoup(result.text, 'lxml')

# image = soup.select("img.mw-file-element")[13]

#找出index[]裡面的圖是多少?
# for i in range(len(image)):
#     print(i)
#     print(image[i]["src"])

# print(image["src"])
# print(image["class"])
# print(image["width"])