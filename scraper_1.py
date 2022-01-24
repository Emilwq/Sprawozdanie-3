from bs4 import BeautifulSoup
import requests

result = requests.get("https://www.google.com/")
print(result.status_code)
src = result.content
soup = BeautifulSoup(src, 'html.parser')
links = soup.find_all("a")
image = soup.find_all("img")


def show_links():
    for link in links:
        if "M" in link.attrs['href']:
            print(link)
            print(link.attrs['href'])

def show_img():
    img_nr = 1
    for img in image:
        print("Zdj nr. "+str(img_nr))
        print(img.attrs['width'])
        print(img.attrs['height'])
        print(img.attrs['alt'])
        if img.attrs['alt'] == "":
            print("Brak tekstu alternatywnego")
        img_nr+=1

show_links()
show_img() 


    

