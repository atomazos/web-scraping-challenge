# web-scraping-challenge

I built a cool web app that scrapes various websites that contains data related to the Mission to Mars and displays the information in a single HTML page. With Jupyter Notebook, I used the BeautifulSoup, Pandas, and Splinter Python libraries to scrape the following websites:

* The latest news title and paragraph text from the NASA Mars News Site.
* The image url for the featured Mars image from JPL Featured Space Image.
* The latest Mars weather tweet from the Mars Weather twitter account.
* The Mars Facts webpage.
* The Mars hemispheres images from the USGS Astrogeology site.

With the scrape_mars.py file, I pythonically (yes, that's a word, for the uninitiated) coded a function declaration called "scrape" to execute the above web scraping, which returns one Python dictionary containing all of the scraped data. Then, in the app.py file, I coded an app route called "/scrape" that basically calls the "scrape"function and stores the data into a Mongo database, which creates a root route / that queries the Mongo database and passes the Mission to Mars data into an HTML template to display the data.


### Webpage Screenshots

<img width="1433" alt="screenshot_one" src="https://user-images.githubusercontent.com/54033512/69487436-6638e080-0e1f-11ea-8cca-7fe3ac487a35.png">
<img width="1357" alt="screen_shot_two" src="https://user-images.githubusercontent.com/54033512/69487442-7fda2800-0e1f-11ea-84e0-14814dd46bbc.png">
<img width="1353" alt="screen_shot_three" src="https://user-images.githubusercontent.com/54033512/69487445-836daf00-0e1f-11ea-88d7-1d0cc020912d.png">
