# Mission to Mars
Scraping, MongoDB and Flask Application

![mission_to_mars_image](https://github.com/ofunkey/Web_Scraping_and_Document_Databases/blob/master/Mission%20to%20Mars/mission_to_mars_im.png)

In this work, a web application that scrapes various websites for data related to the Mission to Mars is created and the information is displayed in a single HTML page.

## 1. Scraping and Analysis Task
* Complete the initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Splinter.

### NASA Mars News
* Scrape the NASA Mars News Site and collect the latest News Title and Paragraph Text. 
```python
[{'news_title': "Robotic Toolkit Added to NASA's Mars 2020 Rover",
  'news Paragraph': "The bit carousel, which lies at the heart of the rover's Sample Caching System, is now aboard NASA's newest rover. "}]
  ```

### JPL Mars Space Images - Featured Image
* Visit and find the image url for the current Featured Mars Image
```python
featured_image_url = 'https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA18614_hires.jpg'
```

### Mars Weather
* Visit the Mars Weather twitter account and scrape the latest Mars weather tweet from the page.
```python
InSight sol 261 (2019-08-21) low -102.4ºC (-152.4ºF) high -26.6ºC (-15.8ºF)
winds from the SSE at 4.9 m/s (11.0 mph) gusting to 16.0 m/s (35.8 mph)
pressure at 7.70 hPa
```

###   Mars Facts
* Visit the Mars Facts webpage and use Pandas to scrape the table containing facts about the planet including Diameter, Mass etc
[mars_fact.html](https://github.com/ofunkey/Web_Scraping_and_Document_Databases/blob/master/Mission%20to%20Mars/mars_fact_table.html)


### Mars Hemispheres
* Visit the USGS Astrogeology site to obtain high resolution images for each of Mar's hemispheres.
```python
[{'title': 'Cerberus Hemisphere Enhanced',
  'img_url': 'https://astrogeology.usgs.gov/cache/images/cfa62af2557222a02478f1fcd781d445_cerberus_enhanced.tif_full.jpg'},
 {'title': 'Schiaparelli Hemisphere Enhanced',
  'img_url': 'https://astrogeology.usgs.gov/cache/images/3cdd1cbf5e0813bba925c9030d13b62e_schiaparelli_enhanced.tif_full.jpg'},
 {'title': 'Syrtis Major Hemisphere Enhanced',
  'img_url': 'https://astrogeology.usgs.gov/cache/images/ae209b4e408bb6c3e67b6af38168cf28_syrtis_major_enhanced.tif_full.jpg'},
 {'title': 'Valles Marineris Hemisphere Enhanced',
  'img_url': 'https://astrogeology.usgs.gov/cache/images/7cf2da4bf549ed01c17f206327be4db7_valles_marineris_enhanced.tif_full.jpg'}]
  ```

## 2. MongoDB and Flask Application
Use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above
* First Jupyter notebook is converted into a Python script called scrape_mars.py with a function called scrape that executes all of the scraping code from above and return one Python dictionary containing all of the scraped data.
* Next, a route called /scrape that will import the scrape_mars.py script is created and called scrape function.
  * Then, the return value in Mongo is stored as a Python dictionary.
* A root route / that queries the Mongo database is created and the mars data is passed into an HTML template to display the data.

* Next a template HTML file called index.html that takes the mars data dictionary is created to display all of the data in the appropriate HTML elements. 
