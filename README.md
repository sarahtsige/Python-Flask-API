# Python-Flask-API
Create API using Python and Flask

## Technologies 
-Python
-Flask 
-PeeWee


## Objective
Objective was to build an API using Flask and PeeWee.  Data set utilized was gatherered from Kaggle.    Data is from the world
happiness report and lists the countries in order of happiness as rated by a hapiness score.  API includes the country name, 
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

'/country/<id>'  - Returns one country with matching the id provided in the URL


'/country/region/<region>' - Return list of countries within the provided region

## Author

Sarah Saleh














