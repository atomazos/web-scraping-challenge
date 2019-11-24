# web-scraping-challenge
## Mission to Mars

Building a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page.

## Step 1: Scraping
mission_to_mars.ipynb: the Jupyter Notebook file that outlines all the scraping. Python libraries used: BeautifulSoup, Pandas, and Splinter

Scrape latest news title and paragraph text from the NASA Mars News Site.
Scrape the image url for the featured Mars image from JPL Featured Space Image.
Scrape the latest Mars weather tweet from the Mars Weather twitter account.
Scrape the Mars Facts webpage.
Scrape Mars hemispheres images from the USGS Astrogeology site.

## Step 2:MongoDB and Flask Application

scrape_mars.py: declares a function called scrape to execute the Step 1 scraping and returns the scraped data.

app.py: creates an app route called /scrape that calls the scrape function and store data in Mongo database; creates a root route / that queries the Mongo database and pass the Mars data into an HTML template to display the data.

index.html: a template HTML file that displays the above outputs in the appropriate HTML elements.
<img width="1433" alt="screenshot_one" src="https://user-images.githubusercontent.com/54033512/69487436-6638e080-0e1f-11ea-8cca-7fe3ac487a35.png">
<img width="1357" alt="screen_shot_two" src="https://user-images.githubusercontent.com/54033512/69487442-7fda2800-0e1f-11ea-84e0-14814dd46bbc.png">
<img width="1353" alt="screen_shot_three" src="https://user-images.githubusercontent.com/54033512/69487445-836daf00-0e1f-11ea-88d7-1d0cc020912d.png">
