from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
import requests

def browser_setup():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

def get_emojis():
    browser = browser_setup()
    url = "https://slackmojis.com/categories/19-random-emojis"

    # Update with stuff
    emoji_data = []

    ##### Headlines #####
    browser.visit(url)
    time.sleep(2)

    html = browser.html
    soup = bs(html, 'html.parser')
    emojis = soup.find_all('li', class_='emoji')

    for emoji in emojis:
        link = emoji.find('a', class_='downloader')
        emoji_name = link.find('div', class_='name').text.strip('\n')
        full_url = 'https://slackmojis.com' + link['href']
        file_name = link['download']
        data = {'name' : emoji_name, 'url' : full_url, 'file': file_name}
        print(data)
        emoji_data.append(data)


    # Close the browser after scraping
    browser.quit()

    return emoji_data
