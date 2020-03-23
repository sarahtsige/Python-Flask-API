# Python-Flask-API
Create API using Python and Flask

## Technologies 
* Python
* Flask 
* PeeWee


## Objective
Objective was to build an API using Flask and PeeWee.  Data set utilized was gathered from Kaggle.    Data is from the 2015 world
happiness report and lists countries and happiness rank as measured by the country's happiness score.  API includes the country name, 
region, happiness ranking, and hapiness score.


Sample response:

```
{
"happiness_score": 4.874,
"id": 100,
"name": "Mongolia",
"rank": 100,
"region": "Eastern Asia"
}
```

## Paths
Paths available to access data are:

'/'  - Returns all countries

'/country/`<id>`'  - Returns one country matching the id provided in the URL


'/country/region/`<id>`' - Return list of countries within the provided region

'/regions/' - Returns the list of regions

'/regions/`<id>`' - Returns the region matching the region id provided

## Author

Sarah Saleh














