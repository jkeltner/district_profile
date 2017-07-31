# District Overview

## Introduction
I created this project because I wanted to be able to see some overview information for my congressional district and compare it to averages in my state and the nation. When I saw there was an API that allowed you to retrieve data from the Census Bureau [American Community Survey](https://www.census.gov/programs-surveys/acs/) I figured it would be a fun project. The goal is to provide a simple way to see some overview information about any congressional district and compare figure with state and national averages.

## Census API Key
In order to run this program you will need to have an API key provided by the Census bureau.It’s relatively easy to get one at [this ist](http://api.census.gov/data/key_signup.html). One you have it create a file names **api_key.py** and enter the following:

`API_KEY = YOUR_API_KEY`

Once you’ve done this, you should be able to run the code here.

## Architecture
To keep this project simple (and the API key out of the client side code), I put all of the API calls one the server side. The client simply makes a request including the state, district, and the name of the chart. The server-side code translates the chart name into the proper query and returns the data needed to produce the chart. I kept this at one call per chart (instead of per data set of for all charts at once) to balance simplicity with speed of page load.

## Technologies
This project relies on a few core technologies:
* Google App Engine
* Python
* JQuery
* Bootstrap
* Charts.js
* Census API (of course!)
    
