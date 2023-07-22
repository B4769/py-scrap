import requests
from bs4 import BeautifulSoup

url = 'https://www.mekina.net'
response = requests.get(url)

content = response.content

def scrape_data(html_code):
    soup = BeautifulSoup(html_code, "html.parser")
    items = soup.find_all("div", class_="col-md-4 col-sm-6 col-xs-6 simple")

    for item in items:
        
        image_tag = item.find("img")
        image_url = image_tag["src"] if image_tag else "Image URL not found"

        
        phone_tag = item.find("a", href=lambda href: href and href.startswith("tel:"))
        phone_number = phone_tag["href"][4:] if phone_tag else "Phone number not found"

        
        text_tag = item.find("h3", itemprop="name").find("a")
        text = text_tag.text.strip() if text_tag else "Text not found"

        price_tag = item.find("div", class_="price")
        price = price_tag.text.strip() if price_tag else "Price not found"

        
        location_tag = item.find("span", itemprop="addressLocality")
        location = location_tag.text.strip() if location_tag else "Location not found"

        
        base_url = 'https://api.telegram.org/bot6041754204:AAGOiKHZVXVEIdvEfxKjMrHtXATRYaDDsLA/sendMessage?chat_id=1449202529&text='
        message = f"{text}\nPrice: {price}\nPhone number: {phone_number}\nLocation: {location}\nImage URL: {image_url}"
        requests.get(base_url + message)

scrape_data(content)
