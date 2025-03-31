import requests
import bs4

response = requests.get("https://en.wikipedia.org/wiki/David_Wojnarowicz")
# print(response.text)

soup = bs4.BeautifulSoup(response.text, "html.parser")

images = soup.select('img')
# print(images)

image_links = []
for img in images:
    src = img.get("src")
    image_links.append(f"https:{src}")
    

figure_image_links = []
figure_images = soup.select("figure a img")
for img in figure_images:
    src = img.get("src")
    print(src)
    figure_image_links.append(f"https:{src}")


import urllib.request 
import urllib.parse 
from urllib.error import HTTPError 


for index, url in enumerate(figure_image_links):
    file_name = 'img_' + str(index) + '.jpg'
    file_path = 'images/'    
    full_path = '{}{}'.format(file_path, file_name)
    print(file_name)
    try:
        urllib.request.urlretrieve(url, full_path)
        pass
    except urllib.error.HTTPError as err:
        print(err.code)
        pass
