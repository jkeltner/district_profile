# Districe Overview

## Introduction
I created this project because I wanted to be able to see some overview information for my congressional district and compare it to averages in my state and the nation. When I saw there was a package for R that allowed you to incorporate data from the Census Burea [American Community Survey](https://www.census.gov/programs-surveys/acs/) I figured it would be a fun project. The goal is to provide a simple way to run a report to see some overview information about any congressional district.

## Files

**district.Rmd** This is the primary file. It is an R Markdown file and when it is Knit it will produce an HTML document with the overview information for the district specific in the paramters section. If you want to contribute to this repository, please leave these paramters set to the CA 27th district (my home district).

**acs_api_key.R** To run this script you will need to get a developer key (http://api.census.gov/data/key_signup.html) Once you've done that, you need to create a acs_api_key.R file with the following line
    api.key.install(key="YOUR_API_KEY")
    
