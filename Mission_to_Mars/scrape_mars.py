from bs4 import BeautifulSoup
from splinter import Browser
import pandas as pd
import time
import requests



def init_browser():
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)
    mars_data = {}

def scrape():
    browser = init_browser()
# MARS NASA NEWS

    url = 'https://mars.nasa.gov/news/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    news_title = soup.find('div', class_="content_title")
    news_p = soup.find('div', class_="rollover_description_inner")

    Title =news_title.text
    News =news_p.text


# JPL Mars Space Images - Featured Image
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'

    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    image = soup.find('article', class_='carousel_item').attrs

    style =str(image['style'])

    base_url = 'https://www.jpl.nasa.gov'
    featured_image_url = base_url + style.split("url")[1].strip(";(')")

#MARS WEATHER

    url = 'https://twitter.com/marswxreport?lang=en'

    response = requests.get(url)
    soup = BeautifulSoup(response.text,'html.parser')

    mars_weather = soup.find_all('div', class_='js-tweet-text-container')[1]
    weather = mars_weather.p.text
    Mars_Weather = "sol 346 (2019-11-16) low -101.5ºC (-150.8ºF) high -23.5ºC (-10.3ºF)\nwinds from the SSE at 4.8 m/s (10.8 mph) gusting to 20.0 m/s (44.7 mph)\npressure at 6.80 hPa"

#MARS FACTS

    url = 'https://space-facts.com/mars/'

    tables = pd.read_html(url)
    df = tables[0]
    df.columns = ['Description', 'Value']
    mars_df = df.set_index("Description")

    Html_table = mars_df.to_html().replace('\n','')

# MARS HEMISPHERES
    url ='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser = Browser('chrome')
    browser.visit(url)
    
    links = browser.find_by_css('.itemLink h3')
    for index in range(len(links)):
        link = browser.find_by_css('.itemLink h3')[index]
        link.click()
        img_link = browser.find_by_css('.downloads a').first
        browser.back()
    
    cereberus_url = 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg'
    schiaparelli_url = 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg'
    syrtis_major_url = 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg'
    valles_url = 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg'
    browser.quit()


    mars_data = {
    "Title": Title,
    "News": News,
    "featured_mars_image": featured_image_url,
    "Mars_Weather": Mars_Weather,
    "Html_table": Html_table,
    "cereberus_url": cereberus_url,
    "schiaparelli_url": schiaparelli_url,
    "syrtis_major_url" : syrtis_major_url,
    "valles_url" : valles_url

}

   
    return mars_data