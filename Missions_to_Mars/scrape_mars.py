from splinter import Browser
from bs4 import BeautifulSoup as bs
import time

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

def scrape_everything():
    browser = init_browser()

    # Update with stuff
    mars_data = {}

    # Headlines
    nasa_url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(nasa_url)
    time.sleep(2)
    html = browser.html
    soup = bs(html, 'html.parser')
    news = soup.find_all('div', class_='list_text')
    mars_news = []
    for news_item in news:
        news_title = news_item.find('div', class_='content_title').text
        news_paragraph = news_item.find('div', class_='article_teaser_body').text
        mars_news.append({'title' : news_title, 'paragraph' : news_paragraph})

    # Update mars_data
    mars_data['headline'] = mars_news[0]['title']
    mars_data['headline_paragraph'] = mars_news[0]['paragraph']

    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_data
